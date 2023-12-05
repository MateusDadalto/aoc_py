import pprint
# holy mother of conversions
path = "day_5.txt"
# path = "test.txt"
maps = {}
seeds = []


def add_to_maps(lines: list[str]):
    source, destination = lines[0].removesuffix('map:').strip().split('-to-')
    dest_values = []
    source_values = []

    for line in lines[1:]:
        d, s, increment = [int(value) for value in line.split()]
        dest_values.append((d, d + increment))
        source_values.append((s, s + increment))

    m = {
        'source': source,
        'destination': destination,
        'source_values': source_values,
        'dest_values': dest_values
    }
    maps[source] = m

def map_source(source: str, value: int):
    m = maps[source]

    for i, (start, end) in enumerate(m['source_values']):
        if start <= value < end:
            delta = value - start
            return m['dest_values'][i][0] + delta, m['destination']
    
    return value, m['destination']
            


with open(path, 'r') as file:
    block = []
    for line in file:
        if line.startswith('seeds:'):
            seeds = [int(seed) for seed in line.removeprefix('seeds:').split()]
            continue

        if line == "\n" or line == '':
            if len(block) > 0:
                add_to_maps(block)
                block = []
            continue

        block.append(line.strip())
    
    add_to_maps(block) ## add last block
    

locations = []
for seed in seeds:
    source = 'seed'
    value = seed
    while source != 'location':
        value, source = map_source(source, value)

    locations.append(value)

print(min(locations))