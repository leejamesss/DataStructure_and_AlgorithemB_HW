# #permutation
# str_list=list(input())
# str_list.sort()
# N=len(str_list)
# result=[0 for i in range(N)]
# used=[False for i in range(N)]
# def dfs(n):
#     if n==N:
#         print(''.join(result))
#     for i in range(N):
#         if not used[i]:
#             result[n]=str_list[i]
#             used[i]=True
#             dfs(n+1)
#             used[i]=False
# dfs(0)


# s=list(input())

# s.sort()
# N=len(s)
# used=[False for i in range(N)]
# result=[0 for i in range(N)]
# def dfs(n):
#     if n==N:
#         print(''.join(result))
#     else:
#         for i in range(N):
#             if not used[i]:
#                 result[n]=s[i]
#                 used[i]=True
#                 dfs(n+1)
#                 used[i]=False



# s=list(input())
# s.sort()
# N=len(s)
# result=[0 for i in range(N)]
# used=[False for i in range(N)]
# def dfs(n):
#     if n==N:
#         print(''.join(result))
#     else:
#             for i in range(N):   #go through all the fill choices 
#                 if not used[i]:  #if the choice is not used
#                     result[n]=s[i]  #fill the choice 
#                     used[i]=True
#                     dfs(n+1)
#                     used[i]=False
# dfs(0)







# s=list(input())
# s.sort()
# N=len(s)
# used=[False for i in range(N)]
# result=[0 for i in range(N)]




