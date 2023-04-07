# Find the difference of the sum of the squares of the first ten natural numbers and the square of the sum of the first ten natural numbers

list1 = []
list2 = []

for i in range(1, 100):
    list1.append(i)
    list2.append(i)

for i in range(99):
    list1[i] = list1[i] ** 2

val = (sum(list2) ** 2) - sum(list1)
print(val)