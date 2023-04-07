prices = []
temp = []
num_books = int(input())
total = 0
for i in range(num_books):
    price = int(input())
    prices.append(price)

prices.sort(reverse=True)

for i in prices:
    temp = prices[:3]
    total += sum(temp) - min(temp)
    del(prices[:3])
    if len(prices) == 1:
        total += sum(prices)
print(total)    