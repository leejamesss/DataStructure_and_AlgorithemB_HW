n = int(input())

def can_form_string(a: str, b: str, c: str) -> bool:
    dp = [True] + [False] * len(b)
    
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[j] = dp[j-1] and b[j-1] == c[i+j-1]
            elif j == 0:
                dp[j] = dp[j] and a[i-1] == c[i+j-1]
            else:
                if a[i-1] == c[i+j-1] and b[j-1] == c[i+j-1]:
                    dp[j] = dp[j] or dp[j-1]
                elif a[i-1] == c[i+j-1]:
                    dp[j] = dp[j]
                elif b[j-1] == c[i+j-1]:
                    dp[j] = dp[j-1]
                else:
                    dp[j] = False
    
    return dp[-1]

for i in range(n):
    str1, str2, Strall = input().split()
    if can_form_string(str1, str2, Strall):
        print(f"Data set {i+1}: yes")
    else:
        print(f"Data set {i+1}: no")

#使用滚动数组
#状态的设计：i表示前i个字母，j表示前j个字母，能否组成c的前i+j个字母
#最后返回dp[-1]即可
