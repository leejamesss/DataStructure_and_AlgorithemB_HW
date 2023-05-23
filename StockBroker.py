
while True:
    n = int(input())
    if n == 0:
        break
    INF = 100
    adj = [[INF for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        adj[_][_] = 0
    for i in range(n):
        lst = list(map(int, input().split()))
        op = lst.pop(0)
        for _ in range(op):
            v = lst.pop(0)
            w = lst.pop(0)
            adj[i][v-1] = w
    for i in range(n):
        for j in range(n):
            for k in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])

    max_lst = []
    for i in range(n):
        max_lst.append(max(adj[i]))

    min_num = min(max_lst)
    if min_num == INF:
        print("disjoint")
        continue

    for i in range(n):
        if max_lst[i] == min_num:
            print(i+1, min_num)

# [1,2,4]
# [1,3,5]
# [2,1,2]
# [2,3,6]
# [3,1,2]
# [3,2,2]
