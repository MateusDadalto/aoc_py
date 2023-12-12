path = "day_12.txt"
# path = "test.txt"

with open(path, 'r') as file:
    grid = [[c for c in line.strip()] for line in file]
    