from functools import reduce

vals = list(map(int, input().split()))
prod = reduce((lambda x, y: x * y), vals)
print(prod)