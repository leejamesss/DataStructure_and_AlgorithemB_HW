from collections import deque

def hopscotch(n, m):
    if n == m:
        return 0, ''
    visited = [False] * 10001
    visited[n] = True
    q = deque([(n, 0, '')])
    while q:
        pos, step, path = q.popleft()
        if pos == m:
            return step, path
        if pos * 3 <= 10000 and not visited[pos * 3]:
            visited[pos * 3] = True
            q.append((pos * 3, step + 1, path + 'H'))
        if pos // 2 >= 1 and not visited[pos // 2]:
            visited[pos // 2] = True
            q.append((pos // 2, step + 1, path + 'O'))

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    k, path = hopscotch(n, m)
    print(k)
    print(path)
