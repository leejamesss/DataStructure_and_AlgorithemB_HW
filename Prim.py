import heapq
INF = 10 ^ 30


class Edge:
    def __init__(self, v=0, w=0):
        self.v = v
        self.w = w

    def __lt__(self, other):
        return self.w < other.w


def HeapPrime(G, n):
    xDist = Edge(0, 0)
    pq = []
    heapq.heapify(pq)
    vDist = [INF] * n
    vUsed = [0 for _ in range(n)]
    doneNum = 0
    totalw = 0
    heapq.heappush(pq, Edge(0, 0))
    while doneNum < n and len(pq) > 0:
        while True:
            xDist = pq[0]
            heapq.heappop(pq)
            if not (vUsed[xDist.v]):
                break
        if vUsed[xDist.v] == 0:
            totalw += xDist.w
            vUsed[xDist.v] = 1
            doneNum += 1
            for i in range(len(G[xDist.v])):
                k = G[xDist.v][i].v
                if vUsed[k] == 0:
                    w = G[xDist.v][i].w
                    if w < vDist[k]:
                        vDist[k] = w
                        heapq.heappush(pq, Edge(k, w))

    if doneNum < n:
        return -1
    return totalw


while True:
    try:
        N = int(input())
        G = [[] for i in range(N)]
        for i in range(N):
            lst = list(map(int, input().split()))
            for j in range(N):
                G[i].append(Edge(j, lst[j]))
        print(HeapPrime(G, N))
    except:
        break
