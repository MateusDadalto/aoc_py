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
for bank in banks:
    (first, i) = get_highest_digit(bank[:-1])
    
    (second, j) = get_highest_digit(bank[(i+1):])
    
    bank_val = first*10 + second
    
    part_1+=bank_val
    
    print(bank, bank_val)

print(part_1)