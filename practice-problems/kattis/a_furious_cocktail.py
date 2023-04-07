num_potions, drinking_time = input().split()
num_potions = int(num_potions)
drinking_time = int(drinking_time)
durations = []
flag = False

for i in range(num_potions):
    dur = int(input())
    durations.append(dur)

durations.sort(reverse=True)

time = max(durations)
durations.remove(time)

for i in range(len(durations)):
    time -= drinking_time
    del(durations[0])

if time > 0:
    print('YES')
else:
    print('NO')