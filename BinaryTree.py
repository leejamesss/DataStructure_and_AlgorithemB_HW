class BinaryTree:
    def __init__(self,data,left = None,right = None):
        self.data,self.left,self.right = data,left,right
    def addLeft(self,tree): #tree是一个二叉树
        self.left = tree    
    def addRight(self,tree): #tree是一个二叉树
        self.right = tree    
    def preorderTraversal(self, op): #前序遍历,op是函数，表示操作
        op(self) #访问根结点
        if self.left: #左子树不为空
            self.left.preorderTraversal(op) #遍历左子树
        if self.right:
            self.right.preorderTraversal(op) #遍历右子树
    def inorderTraversal(self, op): #中序遍历,op是函数，表示操作
        if self.left: #左子树不为空
            self.left.inorderTraversal(op) #遍历左子树
        op(self) #访问根结点
        if self.right:
            self.right.inorderTraversal(op)
    def postorderTraversal(self, op): #后序遍历,op是函数，表示操作
        if self.left: #左子树不为空
            self.left.postorderTraversal(op) #遍历左子树
        if self.right:
            self.right.postorderTraversal(op)
        op(self) #访问根结点
    def levelorderTraversal(self, op): #层次遍历,op是函数，表示操作
        queue = [self] #队列

        while queue:    
            node = queue.pop(0)
