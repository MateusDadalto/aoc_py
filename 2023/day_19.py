from collections import deque
from copy import deepcopy
import json


path = "day_19.txt"
# path = "test.txt"
workflows = {}
LIMIT = 'limit'
DESTINATION = 'destination'
CAT = 'cat'
SIGNAL = 'signal'
START = 'start'
END = 'end'

# def build_bigger_than_fn(cat, limit, destination):

#     return lambda o: destination if o[cat] > limit else None

# def build_smaller_than_fn(cat, limit, destination):

#     return lambda o: destination if o[cat] < limit else None


def parse_rules(rules: list[str]):
    r = []
    condition = ''
    destination = ''
    for entry in rules:
        if ':' in entry:
            condition, destination = entry.split(':')
            cat = condition[0]
            signal = condition[1]
            limit = int(condition[2:])

            r.append({'cat': cat, 'signal': signal,
                     'limit': limit, 'destination': destination})

            # r.append(build_bigger_than_fn(cat, limit, destination) if signal == '>' else build_smaller_than_fn(cat, limit, destination))
        else:
            destination = entry
            r.append({'cat': None, 'destination': destination})
            # r.append(lambda o: destination)

    return r


with open(path, 'r') as file:
    workflow_input, objects = file.read().split('\n\n')

for w in workflow_input.split():
    name, rules = w.split('{')
    rules = rules[:-1].split(',')
    workflows[name] = parse_rules(rules)

# answer = 0
# for o in objects.split():
#     o = o.replace('=', ':').replace('s', '"s"').replace('a', '"a"').replace('m', '"m"').replace('x', '"x"')
#     o = json.loads(o)
#     status = 'in'
#     while status not in ['R', 'A']:
#         for rule in workflows[status]:
#             if rule(o) != None:
#                 status = rule(o)
#                 break

#     if status == 'A':
#         answer += sum(o.values())

# part 2

def update_limit(category, limit, signal):
    if signal == '>' and category[END] > limit:
        return {START: limit + 1, END: category[END]}
    
    if signal == '<' and category[START] < limit:
        return {START: category[START], END: limit - 1}
    
    return None

def calculate_possibilities(limits):
    # print('Calculate:', limits)
    p = 1
    for cat in limits.values():
        p *= (cat[END]+ 1) - cat[START]

    return p

# x,m,a,s
a = deque([('in', {'x': {'start': 1, 'end': 4000}, 'm': {'start': 1, 'end': 4000}, 'a': {
          'start': 1, 'end': 4000}, 's': {'start': 1, 'end': 4000}})])

total = 0
while len(a) > 0:
    current, cat_limits = a.popleft()
    print(current, cat_limits)

    for rule in workflows[current]:
        if rule[CAT] != None:
            cat = rule[CAT]
            new_limit = update_limit(cat_limits[cat], rule[LIMIT], rule[SIGNAL])
            if new_limit:
                if rule[SIGNAL] == '<':
                    cat_limits[cat][START] = rule[LIMIT]
                else:
                    cat_limits[cat][END] = rule[LIMIT]

                nxt_cat_limits = deepcopy(cat_limits)
                nxt_cat_limits[cat] = new_limit
                if rule[DESTINATION] == 'A':
                    total += calculate_possibilities(nxt_cat_limits)
                elif rule[DESTINATION] != 'R':
                    a.append((rule[DESTINATION], nxt_cat_limits))
                    
        elif rule[DESTINATION] == 'A':
            total += calculate_possibilities(cat_limits)
        elif rule[DESTINATION] != 'R':
            a.append((rule[DESTINATION], deepcopy(cat_limits)))
            
print(total)