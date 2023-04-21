n, m = map(int, input().split())

maze = []
for i in range(n):
    row = input().strip()
    maze.append(row)

# 判断是否越界或者遇到墙壁
def is_valid(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if maze[x][y] == '#' or maze[x][y] == 'x':
        return False
    return True

# DFS搜索
def dfs(x, y):
    if x == n - 1 and y == m - 1:
        # 找到出口
        return 1

    count = 0
    # 标记当前位置已经访问过
    maze[x] = maze[x][:y] + 'x' + maze[x][y+1:]

    # 搜索四个方向
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for d in directions:
        nx, ny = x + d[0], y + d[1]
        if is_valid(nx, ny):
            count += dfs(nx, ny)

    # 回溯
    maze[x] = maze[x][:y] + '.' + maze[x][y+1:]
    return count


# 从起点开始搜索
print(dfs(0, 0))
