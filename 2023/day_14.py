path = "day_14.txt"
path = "test.txt"


with open(path, 'r') as file:
    grid = [[c for c in line.strip()] for line in file]

r = len(grid)
c = len(grid[0])

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'O':
            for k in range(1, i + 1):
                if grid[i - k][j] != '.':
                    break
                grid[i - k][j] = 'O'
                grid[i - k + 1][j] = '.'

# print(grid)


answer = [len(grid)-i for j in range(c) for i in range(r) if grid[i][j] == 'O']
print(sum(answer))
