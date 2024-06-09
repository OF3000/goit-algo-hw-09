def find_min_coins(coins,sum):
    min_coins = [0]+[float('inf')] * sum
    coins_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coins_used[i] = coin


    res = {}
    current_sum = sum
    while current_sum > 0:
        coin = coins_used[current_sum]
        if coin in res:
            res[coin] += 1
        else:
            res[coin] = 1
        current_sum -= coin
    
    return res

if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    print (find_min_coins(coins,113))