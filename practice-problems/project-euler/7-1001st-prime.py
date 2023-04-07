# Find the 1001st prime number

list = []
num = 1
flag = True
while flag == True:
    for i in range(1, num):
        if num % i == 0:
            break
        else:
            list.append(num)\

    num += 1

    if len(list) == 1001:
        flag = False

print(list)
