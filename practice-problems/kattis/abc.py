nums = list(map(int, input().split()))
order = input()

a = min(nums)
nums.remove(a)
b = min(nums)
nums.remove(b)
c = nums[0]

for i in order:
    if i == 'A':
        print(a, end=" ")
    elif i == 'B':
        print(b, end=" ")
    else:
        print(c)
