class Edge:
    def __init__(self, v, w):
        self.v, self.w = v, w


def topSort(G):
    n = len(G)
    import queue
    inDegree = [0]*n
    q = queue.Queue()
    for i in range(n):
        for e in G[i]:
            inDegree[e.v] += 1
    for i in range(n):
        if inDegree[i] == 0:
            q.put(i)
    seq = []
    while not q.empty():
        k = q.get()
        seq.append(k)
        for e in G[k]:
            inDegree[e.v] -= 1
            if inDegree[e.v] == 0:
                q.put(e.v)
    if len(seq) != n:
        return None
    else:
        return seq
