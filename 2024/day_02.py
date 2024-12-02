# Code readability improved after submission with chat GPT, check previous commit to read my impossible to read code

path = "day_02.txt"

def is_safe(numbers):
    """
    Checks if the sequence follows the safety rule. 
    A sequence is safe if adjacent differences are between -3 and +3 (exclusive),
    and the direction of differences doesn't alternate.
    
    Returns:
        (bool, int): Tuple of safety status and the index of violation (if any).
    """
    direction = None
    for idx in range(len(numbers) - 1):
        diff = int(numbers[idx]) - int(numbers[idx + 1])

        if 1 <= abs(diff) <= 3:
            new_direction = "ASC" if diff > 0 else "DESC"
            if direction is None:
                direction = new_direction
            elif direction != new_direction:
                return False, idx
        else:
            return False, idx
    return True, -1

def test_with_removed_index(numbers, index_to_remove):
    """
    Checks if the sequence is safe after removing the element at the given index.
    
    Returns:
        bool: Whether the modified sequence is safe.
    """
    reduced_sequence = [numbers[i] for i in range(len(numbers)) if i != index_to_remove]
    is_safe_result, _ = is_safe(reduced_sequence)
    return is_safe_result

with open(path) as file:
    lines = file.readlines()

part_2 = 0
part_1 = 0

for line in lines:
    numbers = line.split()
    is_safe_result, violation_index = is_safe(numbers)

    if is_safe_result:
        part_1 += 1
        part_2 += 1
    else:
        # Check if removing an adjacent element resolves the issue
        if (
            test_with_removed_index(numbers, violation_index) or
            test_with_removed_index(numbers, violation_index + 1) or
            test_with_removed_index(numbers, violation_index - 1)
        ):
            part_2 += 1

print("part 1: ", part_1)
print("part 2: ", part_2)
