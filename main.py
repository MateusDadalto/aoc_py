digits = []
# Open the file in read mode ('r')
with open('day_1.txt', 'r') as file:
    for line in file:
        line_ds = [d for d in line if d.isdigit()]
        digits.append(int(line_ds[0]+line_ds[-1]))

# Now 'contents' contains the contents of the file

print(sum(digits))
