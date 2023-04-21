from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    row = input().strip()
    maze.append(row)

# 判断是否越界或者遇到墙壁
def is_valid(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if maze[x][y] == '#':
        return False
    return True

# BFS搜索
def bfs():
    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            # 找到出口
            return True

        # 搜索四个方向
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return False

# 从起点开始搜索
print(1 if bfs() else 0)
