# 传入plus_num,length_n作为参数：plus_num:加号的数量, length_n:整数的长度
# 考虑构建二维表dp，第j（0-plus_num）行表示加号的数量为j，第i(0-length_n)列表示整数的前i个数字
# n是传入的字符串(代表的是要切分处理的整数)
# 初始条件：
# 1.加号为0         dp[0][k for k  in range(1-length_n-1)]=int(n[:k])
# 2.整数的长度为1    dp[0][0]=0     dp[0][1]=int(n[0:1])  dp[0][2]=int(n[0:2])   dp[0][length_n]=int(n[0:length_n])
# 3.由于i个数字能够插入的加号最多有i-1个，所以当加号的个数j>=i时情况不存在，定义为float("inf")
#
# 4.填充dp的其他地区
#       j(加号个数)<i(数字个数)的情况:填充
#       plus_insert代表加号插入到第plus_insert(1-i-1)个数字的后面，也就是前面的plus_insert个数字要取最小的排列方式，后面的数字就是单独的一个整数int(n[plus_insert:])
#       利用min_lst储存每个加法放置状态下的值(每次for循环 初始化一次)
#       min_lst.append(dp[j-1][plus_insert]+int(n[plus_insert:]))            @优化的小trick:存储一个min，每次大于的就排除
#       dp[j(取值范围：1-plus_num)][i(取值范围：j+1-length_n)]=min(min_lst)
# 5.目标：dp[plus_num][length_n]



def solve(plus_num, length_n):
    global n
    dp = [[float("inf") for _ in range(51)] for _ in range(51)]
    for k in range(1, length_n+1):
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
        break
