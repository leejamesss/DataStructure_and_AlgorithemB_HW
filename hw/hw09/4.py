import heapq

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

# 计算当前节点到终点的估计距离 (这里使用曼哈顿距离)
def manhattan_distance(x, y):
    return abs(x - n + 1) + abs(y - m + 1)

# A*搜索最短路径
def a_star(start_x, start_y):
    pq = [(0, start_x, start_y)]
    heapq.heapify(pq)
    visited = [[False for j in range(m)] for i in range(n)]
    steps = [[0 for j in range(m)] for i in range(n)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while pq:
        f, x, y = heapq.heappop(pq)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if x == n - 1 and y == m - 1:
            # 找到出口，输出路径
            path = [(x, y)]
            while (x, y) != (start_x, start_y):
                for d in directions:
                    px, py = x - d[0], y - d[1]
                    if is_valid(px, py) and steps[px][py] == steps[x][y] - 1:
                        path.insert(0, (px, py))
                        x, y = px, py
            return path

        for d in directions:
            nx, ny = x + d[0], y + d[1]
            if is_valid(nx, ny) and not visited[nx][ny]:
                g = steps[x][y] + 1   # 当前节点到起点的距离
                h = manhattan_distance(nx, ny)   # 当前节点到终点的估计距离
                f = g + h   # 当前节点的 f 值
                heapq.heappush(pq, (f, nx, ny))
                steps[nx][ny] = steps[x][y] + 1

    # 没有找到出口
    return None


# 从起点开始搜索最短路径
path = a_star(0, 0)

if path is None:
    print(0)
else:
    # 输出路径
    for i, j in path:
        print("({},{})".format(i, j), end="")
    print()
