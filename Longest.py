# mx=1010
# maxLen=[[0 for j in range(mx)] for i in range(mx)]
# while True:
#     try:
#         [s1,s2]=input().split()
#         length1,length2=len(s1),len(s2)
#         for i in range(length2+1):
#             maxLen[i][0]=0
#         for j in range(1,length1+1):
#             maxLen[0][j]=0
#         for i in range(1,length1+1):
#             for j in range(1,length2+1):
#                 if s1[i-1]==s2[j-1]:
#                     maxLen[i][j]=maxLen[i-1][j-1]+1
#                 else:
#                     maxLen[i][j]=max(maxLen[i][j-1],maxLen[i-1][j])
#         print(maxLen[length1][length2])
#
#     except:
#         break
#






# mx=1010
# maxLen=[[0 for i in range(mx)] for k in range(mx)]
# [s1,s2]=input().split()
# length1=len(s1)
# length2=len(s2)
# for i in range(1,length1):
#     for k in range(1,length2):
#         if s1[i-1]==s2[k-1]:
#             maxLen[i][k]=maxLen[i-1][k-1]+1
#         else:
#             maxLen[i][k]=max(maxLen[i-1][k],maxLen[i][k-1])
# print(maxLen[length1][length2])





mx = 1010
maxLen = [[0 for i in range(mx)] for k in range(mx)]
while True:
    try:
        [s1,s2]=input().split()
        length1=len(s1)
        length2=len(s2)
        for i in range(length1):
            for k in range(length2):
                if s1[i]==s2[k]:
                    maxLen[i][k]=maxLen[i-1][k-1]+1
                else:
                    maxLen[i][k]=max(maxLen[i-1][k],maxLen[i][k-1])
        print(maxLen[length1-1][length2-1])
    except:
        break

#maxLen(i,j)
