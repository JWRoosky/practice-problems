list = [2, 2, 3, 4]
k = 1
list[k] = list[k + 1]
print(list)
for i in range(len(list[k:])):
    print(list[i])
    list[k + i -1] = list[k + i]
list[-1] = 0
print(list)