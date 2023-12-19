import json


path = "day_19.txt"
# path = "test.txt"
workflows = {}

def build_bigger_than_fn(cat, limit, destination):

    return lambda o: destination if o[cat] > limit else None

def build_smaller_than_fn(cat, limit, destination):

    return lambda o: destination if o[cat] < limit else None

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

            r.append(build_bigger_than_fn(cat, limit, destination) if signal == '>' else build_smaller_than_fn(cat, limit, destination))
        else:
            destination = entry
            r.append(lambda o: destination)

    return r
        


with open(path, 'r') as file:
    workflow_input, objects = file.read().split('\n\n')

for w in workflow_input.split():
    name, rules = w.split('{')
    rules = rules[:-1].split(',')
    workflows[name] = parse_rules(rules)

answer = 0
for o in objects.split():
    o = o.replace('=', ':').replace('s', '"s"').replace('a', '"a"').replace('m', '"m"').replace('x', '"x"')
    o = json.loads(o)
    status = 'in'
    while status not in ['R', 'A']:
        for rule in workflows[status]:
            if rule(o) != None:
                status = rule(o)
                break

    if status == 'A':
        answer += sum(o.values())

print(answer)