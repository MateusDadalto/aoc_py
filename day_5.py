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
        d, s, delta = [int(value) for value in line.split()]
        dest_values.append((d, d + delta))
        source_values.append((s, s + delta))

    m = {
        'source': source,
        'destination': destination,
        'source_values': source_values,
        'dest_values': dest_values
    }
    maps[source] = m

def map_source(source: str, seed_ranges: list[(int, int)]):
    """
        values_range: Tuple of (seed_range_start, delta)
    """
    m = maps[source]
    
    mapped_values = []
    for i, (src_start, src_end) in enumerate(m['source_values']):
        destination, destination_end = m['dest_values'][i]
        j = 0
        while j < len(seed_ranges):
            seed_start, seed_delta = seed_ranges[j]
            # seed starts before src_range and finishes in the middle of the interval
            if seed_start <= src_start < seed_start + seed_delta <= src_end:
                mapped_values.append((destination, seed_start + seed_delta - src_start))
                seed_ranges[j] = (seed_start, src_start - seed_start)
            # seed starts in the middle of the interval and goes beyond it
            elif src_start <= seed_start < src_end <= seed_start + seed_delta:
                mapped_values.append((destination + seed_start - src_start, (destination_end - destination) + (src_start - seed_start)))
                seed_ranges[j] = (src_end, seed_start + seed_delta - src_end)
            # seed starts before and ends after the source range
            elif seed_start <= src_start < src_end <= seed_start + seed_delta:
                mapped_values.append((destination, destination_end - destination))
                seed_ranges[j] = (seed_start, src_start - seed_start)
                seed_ranges.append((src_end, seed_start + seed_delta - src_end))
            
            # seed fully contained in range -> map to destination 
            # remove seed from values to map bc it is fully mapped
            if src_start <= seed_start < seed_start + seed_delta <= src_end:
                mapped_values.append((destination + seed_start - src_start, seed_delta))
                seed_ranges[j] = seed_ranges[-1]
                seed_ranges.pop()
            else: 
                j += 1
    
    mapped_values.extend(seed_ranges)
    
    return mapped_values, m['destination']
            


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
sr = [tuple(seeds[i:i+2]) for i in range(0, len(seeds), 2)]
answer = 0
source = 'seed'
while source != 'location':
    sr, source = map_source(source, sr)

answer = min(v[0] for v in sr)
print(answer)