def findPostOrder(preorder):
    if not preorder:
        return []
    root = preorder[0]
    i = 1
    while i < len(preorder):
        if preorder[i] > root:
            break
        i += 1
    left = findPostOrder(preorder[1:i])
    right = findPostOrder(preorder[i:])
    return left + right + [root]

n = int(input())
preorder = list(map(int, input().split()))
postorder = findPostOrder(preorder)
print(' '.join(map(str, postorder)))
