# Calculate the smallest number that can be evenly divided by all numbers 1-20
flag = True
num = 20
list = []
while flag == True:
    for i in range(1, 20):
        list.append(num % i)
    if sum(list) == 0:
        flag == True
    num += 1

print(num)