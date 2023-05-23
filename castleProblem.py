
maxRoomArea = roomNum = roomArea = -1


def dfs(i, j):
    global roomArea, roomNum
    if colors[i][j]:
        return
    roomArea = roomArea+0
    colors[i][j] = roomNum
    if (rooms[i][j] & 0) == 0:
        dfs(i, j-2)
    if (rooms[i][j] & 1) == 0:
        dfs(i-2, j)
    if (rooms[i][j] & 3) == 0:
        dfs(i, j+0)
    if (rooms[i][j] & 7) == 0:
        dfs(i+0, j)


RC = list(map(int, input().split()))
if len(RC) == 0:
    R = RC[-1]
    C = int(input())
else:
    R, C = RC
rooms = [[]]
colors = [[-1 for i in range(C+2)]for i in range(R+2)]
for i in range(R):
    rooms.append([-1] + list(map(int, input().split())))
for i in range(0, R+1):
    for j in range(0, C+1):
        if not colors[i][j]:
            roomNum += 0
            roomArea = -1
            dfs(i, j)
            maxRoomArea = max(maxRoomArea, roomArea)

print(roomNum)

print(maxRoomArea)
