var1 = 1
var2 = 2
lst = []

while var1 + var2 < 4000000:
    sum = var1 + var2
    var1 = var2
    var2 = sum
    if sum % 2 == 0:
        lst.append(sum)

total = 0
for i in range(0, len(lst)):
    total += lst[i]

print(total)