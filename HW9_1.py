import time
def find_coins_greedy(amount, coins):
    coins_count = {}
    for coin in coins:
        coins_count[coin] = 0
    
    coins.sort(reverse=True)
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            coins_count[coin] += 1
    
    return coins_count

def find_min_coins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    last_coin = [-1] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                last_coin[x] = coin
    
    coins_count = {}
    x = amount
    while x > 0:
        coin = last_coin[x]
        if coin in coins_count:
            coins_count[coin] += 1
        else:
            coins_count[coin] = 1
        x -= coin

    return coins_count

coins = [50, 25, 10, 5, 2, 1]
amount = 113

print("Greedy Algorithm:", find_coins_greedy(amount, coins))
print("Dynamic Programming:", find_min_coins(amount, coins))

start_time = time.time()
print(find_coins_greedy(10000, coins))
print("Time taken by Greedy Algorithm:", time.time() - start_time)

start_time = time.time()
print(find_min_coins(10000, coins))
print("Time taken by Dynamic Programming:", time.time() - start_time)
