import heapq
INF = 1<<30

class Edge:
    def __init__(self,v=0,w=INF):
        self.v=v
        self.w=w
    def __lt__(self,other):
        return self.w<other.w
def HeapPrim(G,n):
    xDist =Edge(0,0)
    pq=[]
    heapq.heapify(pq)
    vDist = [INF for i in range(n)]
    vUsed =[0 for i in range(n)]
    doneNum =0
    totalW=0
    heapq.heappush(pq,Edge(0,0))
    while doneNum<n and len(pq)>0:
        while True:
            xDist = pq[0]
            heapq.heappop(pq)
            if not (vUsed[xDist.v] ==1 and pq!=[]):
                break
        if vUsed[xDist.v] ==0:
            totalW +=xDist.w
            vUsed[xDist.v] =1
            doneNum +=1
            for i in range(len(G[xDist.v])):
                k = G[xDist.v][i].v
                if vUsed[k] ==0:
                    w = G[xDist.v][i].w
                    if w<vDist[k]:
                        vDist[k] =w
                        heapq.heappush(pq,Edge(k,w))
    if doneNum<n:
        return -1
    return totalW


while True:
    try:
        N =int(input())
        G=[[] for i in range(N)]
        for i in range(N):
            lst = list(map(int,input().split()))
            for j in range(N):
                G[i].append(Edge(j,lst[j])) 
        print(HeapPrim(G,N))
    except:
        break
    


    