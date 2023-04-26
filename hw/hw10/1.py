def dfs(x, y):
    # 标记当前瓷砖已经访问过
    visited[x][y] = True
    # 记录访问的瓷砖数
    cnt = 1
    # 遍历当前瓷砖四周的黑色瓷砖
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        # 判断是否越界或者已经访问过或者是红色瓷砖
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and tiles[nx][ny] == '.':
            cnt += dfs(nx, ny)
    return cnt

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # 记录地图状态
    tiles = []
    # 记录起始位置
    start = (0, 0)
    # 初始化地图状态和起始位置
    for i in range(h):
        row = input().strip()
        if '@' in row:
            start = (i, row.index('@'))
        tiles.append(row)
    # 初始化访问状态
    visited = [[False] * w for _ in range(h)]
    print(dfs(*start))
