list = []
for i in range(5):
    num = int(input(f"Enter {5-i} more nums: "))
    list.append(num)
target = int(input("Enter your target sum: "))

try:
    for j in range(len(list)-1):
        for k in range(j, len(list)):
            if list[j] + list[k] == target:
                print(f"The indeces are {j} and {k}")
                raise StopIteration
except StopIteration:
    pass
