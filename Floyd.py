def floyd(G):
    n = len(G)
    INF = 10**9
    prev = [[None for i in range(n)] for j in range(n)]
    dist = [[INF for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            else:
                if G[i][j] != INF:
                    dist[i][j] = G[i][j]
                    prev[i][j] = i
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
                    prev[i][j] = prev[k][j]
    return dist, prev
