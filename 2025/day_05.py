path = "day_05.txt"
# path = "test.txt"

with open(path) as f:
    ranges, ids = f.read().split('\n\n')

range_lines = [tuple(map(int,l.strip().split('-'))) for l in ranges.split("\n")]

def is_in_range(n: int, ranges: tuple[int,int]):
    
    return any([ x <= n <= y for (x,y) in ranges])


counter = 0
for x in ids.split("\n"):
    x = int(x)
    
    if is_in_range(x, range_lines):
        counter += 1
        
        
print("Day 5 part 1:", counter)

def merge_ranges(ranges: tuple[int,int]):
    
    merged_ranges: set[tuple[int, int]] = set([ranges[0]])
    
    for (start, end) in ranges:
        new_ranges: set[tuple[int, int]] = set()
        compare_start = start
        compare_end = end
        
        for (merged_start, merged_end) in merged_ranges:
            
            # starts before and ends inside the range
            if compare_start < merged_start and merged_start <= compare_end <= merged_end:
                if (compare_start, compare_end) in new_ranges:
                    new_ranges.remove((compare_start, compare_end))
                    
                compare_end = merged_end
                new_ranges.add((compare_start, compare_end))
                
            # starts in the inside and ends after the range
            elif merged_start <= compare_start <= merged_end and merged_end < compare_end:
                if (compare_start, compare_end) in new_ranges:
                    new_ranges.remove((compare_start, compare_end))
                    
                compare_start = merged_start
                new_ranges.add((compare_start, compare_end))
            
            # range totally contained in the comparison range 
            elif merged_start <= compare_start and compare_end <= merged_end:
                if (compare_start, compare_end) in new_ranges:
                    new_ranges.remove((compare_start, compare_end))
                    
                compare_start = merged_start
                compare_end = merged_end
                new_ranges.add((compare_start, compare_end))

            # comparison range totally contained in range (I Forgot this consition at first)
            elif compare_start <= merged_start and merged_end <= compare_end:
                new_ranges.add((compare_start, compare_end))
            
            # range not intersecting with comparison range
            else:
                new_ranges.add((compare_start, compare_end))
                new_ranges.add((merged_start, merged_end))
        
        merged_ranges = new_ranges
        
    return merged_ranges
    
result = list(merge_ranges(range_lines))
print(result)

# validation (this made me pick the forgotten condition)
for i in range(len(result)):
    start_i, end_i = result[i]
    for j in range(len(result)):
        start_j, end_j = result[j]
        if i == j:
            continue
        
        if start_j <= start_i <= end_j or start_j <= end_i <= end_j:
            print("ranges not merged", (start_i, end_i), (start_j, end_j))
        

print("Day 5 part 2:", sum([(end - start) + 1 for start,end in result]))
