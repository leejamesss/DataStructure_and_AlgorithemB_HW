# def Ways( w , k ): # 从前k种物品中选择一些，凑成体积w的做法数目
#     if w == 0:
#         return 1
#     if k == 0:
#         return 0
#     if w >= a[k]:
#         return Ways(w, k -1 ) + Ways(w - a[k], k - 1 )
#     else:
#         return Ways(w, k -1 )
# N = int( input() )
# a = [ 0 ]
# for i in range(N):
#     a.append( int(input()))
# print( Ways(40,N) )               递归解法


# # #动态规划解法
# N = int( input() )
# Ways = [ [ 0 for i in range(50) ] for i in range(50) ]
# # Ways[i][j]表示从前j种物品里凑出体积i的方法数
# a = [ 0 ]                               #a 表示每种物品的体积
# for i in range( 1, N+1 ):               #从第一种物品开始
#     a.append( int(input()) )            #a[i]表示第i种物品的体积
#     Ways[0][i] = 1                          #体积为0的时候，只有一种方法
# Ways[0][0] = 1                          #体积为0的时候，只有一种方法
# for w in range( 1, 41 ):                #从体积为1开始
#     for k in range( 1, N+1 ):           #从第一种物品开始
#         Ways[w][k] = Ways[w][k-1]       #不选第k种物品
#         if w-a[k] >= 0:                     #如果体积w-a[k]大于等于0
#             Ways[w][k] += Ways[w-a[k]][k-1] #选第k种物品
# print( Ways[40][N] )                        #输出体积为40的方法数


N = int(input())
Ways = [[0 for i in range(50)] for _ in range(50)]
# 初始化 Ways,默认都是0种方法
# Ways[i][j]表示的是从前j种物品取体积为i的方法数
# i=0   Ways[0][j(0-len(ob_lst))]=1
# j=0   Ways[i(0-V)][0]=1
# 填充剩下的信息
# 如果现在的体积V_required>=V_sum+V_item
#   放入背包    item_num+1       V_sum+=V_item
# 如果现在的体积V_required<V_addition+V_item
#   无法放入背包  item_num 不变


weight_lst = [0]
for i in range(N):
    weight = int(input())
    weight_lst.append(weight)
def Way_cal(V_required,item_num):
   global Ways






# 需要掌握动态规划的多个变量版本
