

# import heapq


# class Edge:
#     def __init__(self, k=0, w=0):
#         self.k = k
#         self.w = w

#     def __lt__(self, other):
#         return self.w < other.w


# bUsed = [0 for i in range(30010)]
# INF = 10000000000
# N, M = map(int, input().split())
# G = [[] for i in range(N+1)]
# for i in range(M):
#     s, e, w = map(int, input().split())
#     G[s].append(Edge(e, w))


# pq = []
# heapq.heapify(pq)
# heapq.heappush(pq, Edge(1, 0))


# while pq != []:
#     p = pq[0]
#     heapq.heappop(pq)
#     if bUsed[p.k]:
#         continue

#     bUsed[p.k] = 1
#     if p.k == N:
#         break
#     L = len(G[p.k])
#     for i in range(L):
#         q = Edge()
#         q.k = G[p.k][i].k
#         if bUsed[q.k]:
#             continue
#         q.w = p.w + G[p.k][i].w
#         heapq.heappush(pq, q)
# print(p.w)


import heapq


class Edge:
    def __init__(self, k=0, w=0):
        self.k = k
        self.w = w

    def __lt__(self, other):
        return self.w < other.w


N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
bUsed = [0 for i in range(30010)]
INF = 1000000
for i in range(M):
    s, e, w = map(int, input().split())
    G[s].append(Edge(e, w))


pq = []
heapq.heapify(pq)
heapq.heappush(pq, Edge(1, 0))

while pq != []:
    p = pq[0]
    heapq.heappop(pq)
    if bUsed[p.k]:
        continue
    bUsed[p.k] = 1
    if p.k == N:
        break
    L = len(G[p.k])
    for i in range(L):
        q = Edge()
        q.k


# while pq != []:
#     p = pq[0]
#     heapq.heappop(pq)
#     if bUsed[p.k]:
#         continue

#     bUsed[p.k] = 1
#     if p.k == N:
#         break
#     L = len(G[p.k])
#     for i in range(L):
#         q = Edge()
#         q.k = G[p.k][i].k
#         if bUsed[q.k]:
#             continue
#         q.w = p.w + G[p.k][i].w
#         heapq.heappush(pq, q)
# print(p.w)
