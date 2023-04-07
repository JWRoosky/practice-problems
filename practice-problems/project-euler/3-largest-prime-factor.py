flag = False
lst = []

def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            flag = False
        else:
            flag = True

for num in range(2, 600851475143):
    check_prime(num)
    if flag == True:
        lst.append(num)

lst.sort()
print(lst[-1])