path = "day_4.txt"
# path = "test.txt"

def calculate_points(intersection: list[int]):
    if len(intersection) == 0:
        return 0
    
    return 2 ** (len(intersection) - 1)

total = 0
with open(path, 'r') as file:
    for line in file:
        line = line.strip().split(':')
        card_id = int(line[0].removeprefix('Card').strip())
        scratch_info = line[1].split('|')
        winning_numbers = [int(n) for n in scratch_info[0].strip().replace('  ', ' ').split(' ')]
        player_numbers = [int(n) for n in scratch_info[1].strip().replace('  ', ' ').split(' ')]
        
        intersection = [a for a in player_numbers if a in winning_numbers]
        total += calculate_points(intersection)
    
print(total)