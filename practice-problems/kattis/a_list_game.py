target_num = int(input())
flag = True
list = []
numeric_list = []
factors = []
counter = 0

def get_factors(n):

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return True

get_factors(target_num)
factors.sort(reverse=True)
del(factors[0])
del(factors[-1])

for i in factors:
    if get_factors(factors[i]):
        counter += 2