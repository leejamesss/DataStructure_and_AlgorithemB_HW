# #longestUpperSubsequence
# N = int(input())
# maxLen = [1 for i in range(N)]
# a = list(map(int,input().split()))
# for i in range(1,N):
# #每次求以第i个数为终点的最长上升子序列的长度
#     for j in range(0,i):
# #察看以第j个数为终点的最长上升子序列
#         if a[i] > a[j]:
#             maxLen[i] = max(maxLen[i],maxLen[j]+1)
# print(max(maxLen))
# #时间复杂度O(N^2)

N=int(input())
a=list(map(int,input().split()))
maxLen=[1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if a[i]>a[j]:
            maxLen[i]=max(maxLen[j]+1,maxLen[i])
print(max(maxLen))


#难在状态的设计
