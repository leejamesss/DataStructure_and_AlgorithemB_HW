class BinaryTree:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def addLeft(self,tree):
        self.left = tree
    def addRight(self,tree):
        self.right = tree
    def preorderTraversal(self,op):
        op(self)
        if self.left:
            self.left.preorderTraversal(op)
        if self.right:
            self.right.preorderTraversal(op)
    def inorderTraversal(self,op):
        if self.left:
            self.left.inorderTraversal(op)
        op(self)
        if self.right:
            self.right.inorderTraversal(op)
    def postorderTraversal(self,op):
        if self.left:
            self.left.postorderTraversal(op)
        if self.right:
            self.right.postorderTraversal(op)
        op(self)


def buildTree(nodes):
    nodesPtr=0
    def build(level):
        nonlocal nodesPtr
        tree=BinaryTree(nodes[nodesPtr][1])
        nodesPtr+=1
        if nodesPtr<len(nodes) and nodes[nodesPtr][0]==level+1:
            if nodes[nodesPtr][1]!="0":
                tree.addLeft(build(level+1))
            else:
                nodesPtr+=1
        if nodesPtr<len(nodes) and nodes[nodesPtr][0]==level+1:
            tree.addRight(build(level+1))
        return tree
    return build(0)

nodes=[]

while True:
    try:
        s=input().rstrip()
        nodes.append((len(s)-1,s.strip()))
        if s=="":
            break
    except:
        break   

tree=buildTree(nodes)
tree.preorderTraversal(lambda x:print(x.data,end=" "))
print()
tree.inorderTraversal(lambda x:print(x.data,end=" "))
print()
tree.postorderTraversal(lambda x:print(x.data,end=" "))
print()

