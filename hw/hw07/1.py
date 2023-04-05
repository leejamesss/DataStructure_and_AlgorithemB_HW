class BinaryTree:
    def __init__(self,data,left = None,right = None):
        self.data,self.left,self.right = data,left,right

    def postorderTravel(self,op):
        if self.left:
            self.left.postorderTravel(op)
        if self.right:
            self.right.postorderTravel(op)
        op(self)
    @staticmethod
    def buildTree(preorder, inorder):
        if not preorder:
            return None
        root = BinaryTree(preorder[0])
        i = inorder.index(preorder[0])
        root.left =BinaryTree.buildTree(preorder[1:i+1],inorder[:i])
        root.right =BinaryTree.buildTree(preorder[i+1:],inorder[i+1:])
        return root

while True:
    try:
        p = input()
        i = input()
        root = BinaryTree.buildTree(p,i)  # 创建类实例后调用方法
        root.postorderTravel(lambda x:print(x.data,end=''))
        print()
    except :
        break
