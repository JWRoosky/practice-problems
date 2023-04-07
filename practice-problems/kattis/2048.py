grid = [[]]

for i in range(4):
    grid[i] = [int(x) for x in input().split()]

direction = int(input())


if direction == 0:
    for j in range(4):
        for k in range(4):
            if k == 1:
                continue
            if grid[j][k] == grid[j][k-1]:
                
                grid[j][k-1] *= 2
print(grid)