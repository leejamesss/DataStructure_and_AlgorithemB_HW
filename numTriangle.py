#numTriangle



# n = int(input())
# D = []
# def MaxSum(i,j):
#     if i == n-1:
#         return D[i][j]
#     x = MaxSum(i+1,j)
#     y = MaxSum(i+1,j+1)
#     return max(x,y) + D[i][j]
# def main():
#     for i in range(n):
#         lst = list(map(int,input().split()))
#     D.append(lst)
#     print(MaxSum(0,0))
# main()


#递归



# n = int(input())
# D = []
# maxSum = [[-1 for j in range(i+1)] for i in range(n)]
# def MaxSum(i,j):
#     if i == n-1:
#         return D[i][j]
#     if maxSum[i][j] != -1:
#         return maxSum[i][j]
#     x = MaxSum(i+1,j)
#     y = MaxSum(i+1,j+1)
#     maxSum[i][j] = max(x,y) + D[i][j]
#     return maxSum[i][j]
# for i in range(n):
#     lst = list(map(int,input().split()))
#     D.append(lst)
# print(MaxSum(0,0))







#记忆化搜索



#递推：循环

# n = int(input())
# D = []
# maxSum = [[-1 for j in range(i+1)] for i in range(n)]
# def main():
#     for i  in range(n):
#         lst = list(map(int,input().split()))
#         D.append(lst)
#     for i in range(n):
#         maxSum[n-1][i] = D[n-1][i]
#     for i in range(n-2,-1,-1):
#         for j in range(0,i+1):
#             maxSum[i][j] =max(maxSum[i+1][j],maxSum[i+1][j+1]) + D[i][j]
#     print(maxSum[0][0])
# main()



#空间优化:只用一维数组（滚动数组）
# n = int(input())
# D = []
# def main():
#     for i in range(n):
#         lst = list(map(int,input().split()))
#         D.append(lst)
#     maxSum = D[n-1]
#     for i in range(n-2,-1,-1):
#         for j in range(0,i+1):
#             maxSum[j] = max(maxSum[j],maxSum[j+1]) + D[i][j]
#     print(maxSum[0])
# main()

#递归、递推、状态转移方程
#递归：自顶向下
#递推：自底向上
#状态转移方程：f(i,j) = max(f(i+1,j),f(i+1,j+1)) + D[i][j]
#递归：f(i,j) = max(f(i+1,j),f(i+1,j+1)) + D[i][j]
#递推：f(i,j) = max(f(i+1,j),f(i+1,j+1)) + D[i][j]
#空间优化：f(i,j) = max(f(i+1,j),f(i+1,j+1)) + D[i][j]

#人人为我（未知值）
#我（未知值）为人人


#动态规划的特点
#最优子结构
#无后效性






















