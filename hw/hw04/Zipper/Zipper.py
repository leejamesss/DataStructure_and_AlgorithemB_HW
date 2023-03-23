
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





# n = int(input())

# def can_form_string(a: str, b: str, c: str) -> bool:
#     dp = [[False] * (len(b) + 1) for _ in range(len(a) + 1)]
    
#     # 初始化边界条件
#     dp[0][0] = True
#     for i in range(1, len(a) + 1):
#         dp[i][0] = dp[i-1][0] and a[i-1] == c[i-1]
#     for j in range(1, len(b) + 1):
#         dp[0][j] = dp[0][j-1] and b[j-1] == c[j-1]
    
#     # 填充dp表
#     for i in range(1, len(a) + 1):
#         for j in range(1, len(b) + 1):
#             if a[i-1] == c[i+j-1] and b[j-1] == c[i+j-1]:
#                 dp[i][j] = dp[i-1][j] or dp[i][j-1]
#             elif a[i-1] == c[i+j-1]:
#                 dp[i][j] = dp[i-1][j]
#             elif b[j-1] == c[i+j-1]:
#                 dp[i][j] = dp[i][j-1]
#             else:
#                 dp[i][j] = False
    
#     return dp[-1][-1]

# for i in range(n):
#     str1, str2, Strall = input().split()
#     if can_form_string(str1, str2, Strall):
#         print(f"Data set {i+1}: yes")
#     else:
#         print(f"Data set {i+1}: no")


# n = int(input())

# def can_form_string(a: str, b: str, c: str) -> bool:
#     dp = [True] + [False] * len(b)
    
#     for i in range(len(a) + 1):
#         for j in range(len(b) + 1):
#             if i == 0 and j == 0:
#                 continue
#             elif i == 0:
#                 dp[j] = dp[j-1] and b[j-1] == c[i+j-1]
#             elif j == 0:
#                 dp[j] = dp[j] and a[i-1] == c[i+j-1]
#             else:
#                 if a[i-1] == c[i+j-1] and b[j-1] == c[i+j-1]:
#                     dp[j] = dp[j] or dp[j-1]
#                 elif a[i-1] == c[i+j-1]:
#                     dp[j] = dp[j]
#                 elif b[j-1] == c[i+j-1]:
#                     dp[j] = dp[j-1]
#                 else:
#                     dp[j] = False
    
#     return dp[-1]

# for i in range(n):
#     str1, str2, Strall = input().split()
#     if can_form_string(str1, str2, Strall):
#         print(f"Data set {i+1}: yes")
#     else:
#         print(f"Data set {i+1}: no")




# n = int(input())

# def can_form_string(a: str, b: str, c: str) -> bool:
#     if len(a) + len(b) != len(c):
#         return False

#     dp = [True] + [False] * len(b)
    
#     for i in range(len(a) + 1):
#         prev_dp_j = dp[0]
#         dp[0] = dp[0] and a[i-1] == c[i-1] if i > 0 else True
        
#         for j in range(1, len(b) + 1):
#             prev_dp_i_j = dp[j]
            
#             if i == 0:
#                 dp[j] = dp[j-1] and b[j-1] == c[i+j-1]
#             else:
#                 if a[i-1] == c[i+j-1] and b[j-1] == c[i+j-1]:
#                     dp[j] = prev_dp_j or dp[j-1]
#                 elif a[i-1] == c[i+j-1]:
#                     dp[j] = prev_dp_j
#                 elif b[j-1] == c[i+j-1]:
#                     dp[j] = dp[j-1]
#                 else:
#                     dp[j] = False
            
#             prev_dp_j = prev_dp_i_j
        
#     return dp[-1]

# for i in range(n):
#     str1, str2, Strall = input().split()
#     if can_form_string(str1, str2, Strall):
#         print(f"Data set {i+1}: yes")
#     else:
#         print(f"Data set {i+1}: no")




# n = int(input())

# def can_form_string(a: str, b: str, c: str) -> bool:
#     if len(a) + len(b) != len(c):
#         return False

#     dp = [True] + [False] * len(b)
    
#     for i in range(len(a) + 1):
#         prev_dp_j = dp[0]
#         dp[0] = dp[0] and a[i-1] == c[i-1] if i > 0 else True
        
#         for j in range(1, len(b) + 1):
#             prev_dp_i_j = dp[j]
            
#             if i == 0:
#                 dp[j] = dp[j-1] and b[j-1] == c[i+j-1]
#             else:
#                 if a[i-1] == c[i+j-1] and b[j-1] == c[i+j-1]:
#                     dp[j] = prev_dp_j or dp[j-1]
#                 elif a[i-1] == c[i+j-1]:
#                     dp[j] = prev_dp_j
#                 elif b[j-1] == c[i+j-1]:
#                     dp[j] = dp[j-1]
#                 else:
#                     dp[j] = False
            
#             prev_dp_j = prev_dp_i_j
        
#     return dp[-1]

# for i in range(n):
#     str1, str2, Strall = input().split()
#     if can_form_string(str1, str2, Strall):
#         print(f"Data set {i+1}: yes")
#     else:
#         print(f"Data set {i+1}: no")






















# def can_form_string(a: str, b: str, c: str) -> bool:
#     if len(a) == 0:
#         return b == c
#     if len(b) == 0:
#         return a == c
#     if a[0] == c[0] and b[0] == c[0]:
#         return can_form_string(a[1:], b, c[1:]) or can_form_string(a, b[1:], c[1:])
#     if a[0] == c[0]:
#         return can_form_string(a[1:], b, c[1:])
#     if b[0] == c[0]:
#         return can_form_string(a, b[1:], c[1:])
#     return False
# for i in range(n):
#     str1,str2,Strall=input().split()
#     if can_form_string(str1,str2,Strall):
#             print(f"Data set {i+1}: yes")
#     else:
#             print(f"Data set {i+1}: no")
    







    

















