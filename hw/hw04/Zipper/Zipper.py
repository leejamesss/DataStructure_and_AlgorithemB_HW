
#利用动归思想储存算好的结果
#dp[i][j]表示a的前i个字符和b的前j个字符能否组成c的前i+j个字符


# #输出
# n=int(input())
# for i in range(n):
#     a,b,c=input().split()
#     dp=[[False for i in range(201)]for j in range(201)]
# #初始化
#     dp[0][0]=True
#     for i in range(1,len(a)+1):
#         if a[i-1]==c[i-1] and dp[i-1][0]:
#             dp[i][0]=True
#     for i in range(1,len(b)+1):
#         if b[i-1]==c[i-1] and dp[0][i-1]:
#             dp[0][i]=True
# #动归
# #i表示a的前i个字符，j表示b的前j个字符
# #遍历a和b的所有字符

#     for i in range(1,len(a)+1):
#         for j in range(1,len(b)+1):
#             if (dp[i-1][j] and a[i-1]==c[i+j-1]) or (dp[i][j-1] and b[j-1]==c[i+j-1]):
#                 dp[i][j]=True
#             else:
#                 dp[i][j]=False
#     if dp[len(a)][len(b)]:
#         print(f"Data set {i+1}: yes")
#     else:
#         print(f"Data set {i+1}: no")




















    

















