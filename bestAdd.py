
def solve(plus_num, length_n):
    global n
    dp = [[float("inf") for _ in range(51)] for _ in range(51)]
    for k in range(1, length_n + 1):
        dp[0][k] = int(n[:k])
    dp[0][0] = 0
    for _ in range(1, plus_num + 1):
        dp[_][0] = 0
    for j in range(1, plus_num + 1):
        for i in range(j + 1, length_n + 1):
            min_lst = []
            for plus_insert in range(1, i):
                min_lst.append(dp[j - 1][plus_insert] + int(n[plus_insert:i]))
            dp[j][i] = min(min_lst)
    return dp[plus_num][length_n]


while True:
    try:
        m = int(input())
        n = input()
        print(solve(m, len(n)))
    except Exception as e:
        print("Error:", e)
        break