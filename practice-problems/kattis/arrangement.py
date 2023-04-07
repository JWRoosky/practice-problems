import math


rooms = int(input())
teams = int(input())
lst = []
for i in range(teams):
    lst.append(i + 1)

lst.reverse()

for i in len(lst):
    