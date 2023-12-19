from collections import deque
from copy import deepcopy
import json

path = "day_19.txt"
workflows = {}
LIMIT = 'limit'
DESTINATION = 'destination'
CAT = 'cat'
SIGNAL = 'signal'
START = 'start'
END = 'end'


def build_bigger_than_fn(cat, limit, destination):

    return lambda o: destination if o[cat] > limit else None


def build_smaller_than_fn(cat, limit, destination):

    return lambda o: destination if o[cat] < limit else None


def parse_rules(rules: list[str], part_2):
    r = []
    condition = ''
    destination = ''
    for entry in rules:
        if ':' in entry:
            condition, destination = entry.split(':')
            cat = condition[0]
            signal = condition[1]
            limit = int(condition[2:])

            if part_2:
                r.append({CAT: cat, SIGNAL: signal,
                          LIMIT: limit, DESTINATION: destination})
            else:
                r.append(build_bigger_than_fn(cat, limit, destination) if signal ==
                         '>' else build_smaller_than_fn(cat, limit, destination))
        else:
            destination = entry
            if part_2:
                r.append({CAT: None, DESTINATION: destination})
            else:
                r.append(lambda o: destination)

    return r


def parse_input(workflow_input, part_2):
    workflows = {}
    for w in workflow_input.split():
        name, rules = w.split('{')
        rules = rules[:-1].split(',')
        workflows[name] = parse_rules(rules, part_2)

    return workflows


def part_1(workflow_input, objects):
    workflows = parse_input(workflow_input, False)

    answer = 0
    for o in objects.split():
        o = o.replace('=', ':').replace('s', '"s"').replace(
            'a', '"a"').replace('m', '"m"').replace('x', '"x"')
        o = json.loads(o)
        status = 'in'
        while status not in ['R', 'A']:
            for rule in workflows[status]:
                if rule(o) != None:
                    status = rule(o)
                    break

        if status == 'A':
            answer += sum(o.values())

    return answer

# part 2 logic from this point forward - there is a bit of part 2 logic above in the parse_rules


def update_limit(category, limit, signal):
    """
    Upgrade limit will create new limit range for that category.
    If the category is totally out of the rule it will return None
    """
    if signal == '>' and category[END] > limit:
        return {START: limit + 1, END: category[END]}

    if signal == '<' and category[START] < limit:
        return {START: category[START], END: limit - 1}

    return None


def calculate_possibilities(limits):
    """
        The possible values are all the ones in the limit range for each category.
        So we multiply the range size for each category.
        for example, if we had no restrictions, the possible values would be 4000*4000*4000*4000
    """
    p = 1
    for cat in limits.values():
        p *= (cat[END] + 1) - cat[START]

    return p


def part_2(workflow_input):
    workflows = parse_input(workflow_input, True)

    # Let's start traversing our graph, the beginning will be in the 'IN' node
    # deque is being used here so that we can always easily get the first element (FIFO)
    q = deque([(
        'in',
        {
            'x': {START: 1, END: 4000},
            'm': {START: 1, END: 4000},
            'a': {START: 1, END: 4000},
            's': {START: 1, END: 4000}
        }
    )])

    total = 0
    while len(q) > 0:
        # Current node e.g.: 'in'
        # Category limits: the range
        current_node, cat_limits = q.popleft()

        # For each rule in our node
        for rule in workflows[current_node]:
            # If this rule as a category (x,m,a,s) it means it is in the format CAT < LIMIT or CAT > LIMIT e.g.: s<1351
            if rule[CAT] != None:
                cat = rule[CAT]
                new_limit = update_limit(
                    cat_limits[cat], rule[LIMIT], rule[SIGNAL])
                # If we have a new limit, it means that a part of the current limit fits the rule, let's update stuff
                if new_limit:
                    # This is for the part of the category that DOES NOT FIT in the rule 
                    # that will continue in the NEXT rule in this for loop (line 129)
                    if rule[SIGNAL] == '<':
                        cat_limits[cat][START] = rule[LIMIT]
                    else:
                        cat_limits[cat][END] = rule[LIMIT]

                    # for the part that DO fit the rule
                    # If destination is the approval of the object
                    # lets calculate the possibilities for the cat_limits we just created
                    # they are the ones getting approved
                    nxt_cat_limits = deepcopy(cat_limits)
                    nxt_cat_limits[cat] = new_limit
                    if rule[DESTINATION] == 'A':
                        total += calculate_possibilities(nxt_cat_limits)
                    # If destination is not 'A' and not 'R' let's add the next node to our processing queue
                    # let's add another node in the queue to be processed
                    elif rule[DESTINATION] != 'R':
                        q.append((rule[DESTINATION], nxt_cat_limits))

            # If this rule has no category it is a direct mapping, which can be 'A', 'some_node' or 'R'
            # Let's calculate the total possibilities for the limits we have if it is 'A'.
            elif rule[DESTINATION] == 'A':
                total += calculate_possibilities(cat_limits)
            # If destination is not 'A' and not 'R' let's add the next node to our processing queue
            elif rule[DESTINATION] != 'R':
                q.append((rule[DESTINATION], deepcopy(cat_limits)))

    return total


with open(path, 'r') as file:
    workflow_input, objects = file.read().split('\n\n')

print("Part 1:", part_1(workflow_input, objects))
print("Part 2:", part_2(workflow_input))
