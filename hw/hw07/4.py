class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px
while True:
    try:
        n, m = map(int, input().split())
        uf = UnionFind(n)
        count = n
        ice = set(range(1, n+1))

        for i in range(m):
            x, y = map(int, input().split())
            px, py = uf.find(x-1), uf.find(y-1)
            if px == py:
                print("Yes")
            else:
                uf.union(x-1, y-1)
                count -= 1
                ice.discard(py+1)
                print("No")

        print(count)
        print(*sorted(ice))
    except:
        break
