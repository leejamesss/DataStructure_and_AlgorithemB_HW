from queue import Queue

a, b, c = map(int, input().split())
q = Queue()
q.put((0, 0, []))  # (当前状态下A瓶中的水量，B瓶中的水量，操作列表)

visited = set()  # 记录访问过的状态

while not q.empty():
    wa, wb, actions = q.get()
    if wa == c or wb == c:  # 找到目标状态，输出解
        print(len(actions))
        for action in actions:
            print(action)
        break
    if (wa, wb) in visited:  # 避免重复状态
        continue
    visited.add((wa, wb))
    if wa < a:  # FILL(1)
        q.put((a, wb, actions + ['FILL(1)']))
    if wb < b:  # FILL(2)
        q.put((wa, b, actions + ['FILL(2)']))
    if wa > 0:  # DROP(1)
        q.put((0, wb, actions + ['DROP(1)']))
    if wb > 0:  # DROP(2)
        q.put((wa, 0, actions + ['DROP(2)']))
    # POUR(i,j) 操作需要分情况讨论
    if wa > 0 and wb < b:  # POUR(1,2)
        amount = min(wa, b - wb)
        q.put((wa - amount, wb + amount, actions + ['POUR(1,2)']))
    if wb > 0 and wa < a:  # POUR(2,1)
        amount = min(wb, a - wa)
        q.put((wa + amount, wb - amount, actions + ['POUR(2,1)']))
else:
    print('impossible')
