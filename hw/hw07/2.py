def count_binary_trees(n):
    dp = [1, 1]
    for i in range(2, n+1):
        count = 0
        for j in range(i):
            count += dp[j] * dp[i-j-1]
        dp.append(count)
    return dp[n]

print(count_binary_trees(int(input())))
