path = "day_03.txt"
# path = "test.txt"

with open(path) as f:
    banks = [b.strip() for b in f.readlines()]
    
def get_highest_digit(bank: str):
    highest = 0
    highest_i = 0
    for i in range(len(bank)):
        current = int(bank[i])
        
        if current > highest:
            highest = current
            highest_i = i

    return (highest, highest_i)

part_1 = 0
# for bank in banks:
#     (first, i) = get_highest_digit(bank[:-1])
    
#     (second, j) = get_highest_digit(bank[(i+1):])
    
#     bank_val = first*10 + second
    
#     part_1+=bank_val
    
#     print(bank, bank_val)

# print(part_1)

def get_highest_combination(bank, size):
    acc = ''
    temp = bank
    for end_index in range(size - 1, -1, -1):
        # print(end_index, temp)
        if (end_index != 0):
            (digit, new_index) = get_highest_digit(temp[: - end_index])
        else:
            (digit, new_index) = get_highest_digit(temp)

        acc = acc + str(digit)
        
        temp = temp[new_index+1:]
        # print(acc, len(acc), temp)
            
    print(bank, acc)
    
    return int(acc)

part_2 = 0
for bank in banks:
    part_2 += get_highest_combination(bank, 12)
    # (first, i) = get_highest_digit(bank[:-11])
    # (second, j) = get_highest_digit(bank[i+1: -10])
    # (third, k) = get_highest_digit(bank[j+1: -9])
    
print(part_2)
