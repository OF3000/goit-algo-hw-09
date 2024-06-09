def find_coins_greedy(coins,sum):
    res = {}
    for c in coins:
        while c <= sum:
            sum = sum - c
            if res.get(c):
                res[c] =+ 1
            else:
                res[c] = 1

    return res


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    print (find_coins_greedy(coins,113))

   
