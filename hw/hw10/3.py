from collections import deque

def canFinish(numCourses, prerequisites):
    # 初始化入度数组和邻接表
    indegrees = [0 for _ in range(numCourses)]
    adjacency = [[] for _ in range(numCourses)]
    # 填充入度数组和邻接表
    for cur, pre in prerequisites:
        indegrees[cur] += 1
        adjacency[pre].append(cur)
    # 初始化队列
    queue = deque()
    # 将所有入度为0的节点入队
    for i in range(len(indegrees)):
        if not indegrees[i]:
            queue.append(i)
    # 拓扑排序
    while queue:
        pre = queue.popleft()
        numCourses -= 1
        for cur in adjacency[pre]:
            indegrees[cur] -= 1
            if not indegrees[cur]:
                queue.append(cur)
    return not numCourses

while True:
    try:
        line = input().strip()
        if not line:
            continue
        n, m = map(int, line.split())
        prerequisites = []
        for _ in range(m):
            a, b = map(int, input().split())
            prerequisites.append([a, b])
        print(canFinish(n, prerequisites))
    except:
        break
