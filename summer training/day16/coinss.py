#input:[2,3,5,6]
#output:11
def subset_sum(coins, target):
    dp = [False] * (target + 1)
    dp[0] = True
    
    for coin in coins:
        for j in range(target, coin - 1, -1):
            if dp[j - coin]:
                dp[j] = True
    
    return dp[target]

coins = [2, 3, 5, 6]
target = 12

if subset_sum(coins, target):
    print("yes")
else:
    print("no")
