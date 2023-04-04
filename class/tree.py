#直观表示法
class Tree:
  def _init__(self,data,*subtrees):
    self.data=data
    self.subtrees=list(subtrees)
    
  def addSubTree(self,tree):
    self.subtrees.append(tree)
  def preorderTraversal(self,op):
    op(self)
    for t in self.subtrees:
      t.preorderTraversal(op)
    op(self)
  def printTree(self,level=0):
    print("\t" *level +str(self.data))
    for t in self.subtrees:
      t.printTree(level+1)
  def buildTree(level):
    global nodesPtr,nodes
    tree=Tree(nodes[nodePtr][1]
    nodesPtr+=1
    while nodesPtr<len(nodes) and nodes[nodesPtr][0]==level+1:
      tree..addSubTree(buildTree(level+1))
    return tree
 
              
              
  nodes=[]
  while True:
    try:
      s=input().rstrip()
      nodes.append((len(s)-1,s.strip()))
    except:
      break
 nodesPtr=0
 print(nodes)
 tree=buildTree(0)
             
              
  
  
  
#父亲表示法（并查集）

  
