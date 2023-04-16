def findPostOrder(preorder):     
    if not preorder:            #如果preorder是空的，就返回空的list
        return []           
    root = preorder[0]          #根节点是preorder的第一个元素
    i = 1                       #i是preorder中第一个大于root的元素的下标
    while i < len(preorder):    #找到第一个大于root的元素
        if preorder[i] > root:  
            break
        i += 1                  
    left = findPostOrder(preorder[1:i])#递归地找左子树的后序遍历
    right = findPostOrder(preorder[i:])#递归地找右子树的后序遍历
    return left + right + [root]        #左子树的后序遍历+右子树的后序遍历+根节点

n = int(input())                    
preorder = list(map(int, input().split()))  
postorder = findPostOrder(preorder) #找后序遍历
print(' '.join(map(str, postorder)))    #输出后序遍历
