COINS = [10, 5, 1]

while True:
    amount = int(input("Amount to exchange: "))
    if amount > 0:
        break

print('PromptPay Payment:',amount,'baht')
print("You will receive:")
index = 0
while index < len(COINS):
    coin = COINS[index]
    count = amount // coin
    if count:
        print(count, 'x', coin, 'baht')
    amount = amount % coin
    index = index + 1
