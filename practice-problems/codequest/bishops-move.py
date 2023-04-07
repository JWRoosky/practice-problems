cases = int(input())
for i in range(cases):
    grid = list(map(int, input().split(',')))
    startingPos = list(map(int, input().split(',')))
    for j in startingPos:
        if j < 1 or j > grid[0] or j > grid[1]:
            print("No")
            break
    endingPos = list(map(int, input().split(',')))
    for j in endingPos:
        if j < 1 or j > grid[0] or j > grid[1]:
            print("No")
            break
    dif = abs(startingPos[0] - startingPos[1])
    dif2 = abs(endingPos[0] - endingPos[1])
    if dif == dif2:
        print('Yes')
    else:
        print("No")