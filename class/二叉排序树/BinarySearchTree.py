#元素的添加、删除、查找
#二叉查找树：中序遍历序列是递增序列<=>二叉树是二叉搜索树


#二叉排序树查找



#二叉排序树插入（递归插入）

#删除
#1、叶子：直接删除
#2、只有1子节点：左/右边的来替换位置
#3、有两个子节点：


class  BinarySearchTree:
  class Node:
    def __init__(self,key,data,left=None,right=None):
      self.key,self.value,self.left,self.right=key,data,left,right
  def __init__(self,less=lambda x,y:x<y):
    self.root,self.size=None,0
    self.less=less
  def _find(self,key):
    def find(root,father):
      if self.less(key,root.key):
        if root.left:
          return find(root.left,root)
        else:
          return None,None 
      elif self.less(root.key,key):
        if root.right:
          return find(root.right,root)
        else:
          return None,None 
      else:
        return root,father
    if self.root is None:
      return None,None
    return find(self.root,None)
  def _insert(self,key,data):
    def insert(root):
      if self.less(key,root.key):
        if root.left is None:
          root.left =BinarySearchTree.Node(key,data)
          return True
        else:
          return insert(root.left）
      elif self.less(root.key,key):
        if root.right is None:
           root.right = BinarySearchTree.Node(key,data)
           return True
        else:
          return insert(root.right)
      else:
        root.value = data
        return False
 def _findMin(self,root,father):
   if root.right is None:
     return root,father
   else:
     return self._findMax(root.right,father)
 def pop(self,key):
   nd,father=self._find(key)
   if nd is None:
     raise Exception("Key not found")
   else:
     self.size-=1
     self._deleteNode(nd,father)
     return nd.value
 def _deleteNode(self,nd,father):
   if nd.left and nd.right:
     minNd,father=self._findMin(nd.right,nd)
     nd.key,nd.value= minNd.key,minNd.value
     self._deleteNode(minNd,father)
   elif nd.left:
     if father and father.left is nd:
       father.left=nd.left
     elif father and father.right is nd:
       father.right=nd.left
     else:
       self.root=nd.left
   elif nd.right:
     if father and father.right is nd:
       father.right = nd.right 
     elif father and father.left is nd:
       father.left = nd.right 
     else:
       self.root=nd.right
   else:
     if father and father.left is nd:
       father.left=None
     elif father and father.right is nd:
       father.right=None
     else:
       self.root=None 
def _inorderTraversal(self):
  def inorderTraversal(root):
    if root.left:
      yield from inorderTraversal(root.left)
    yield root.key,root.value
    if root.right:
      yield from inorderTraversal(root.right)
    if self.root is None：
      return 
    yield from inorderTraversal(self.root)
def __contains__(self,key):
  return self._find(key)[0] is not None
def __iter__(self):
  return self._inorderTraversal()
def __getitem__(self,key):
  nd,father=self._find(key)
  if nd is None:
    raise Exception("key not found")
  else:
    return nd.value
def __setitem__(self,key,data):
  nd,father=self._find(key)
  if nd is None:
    self._insert(key,data)
  else:
    nd.value=data
def __len__(self)：
  return self.size
 
                        
##############################################                       
                        
                        
import random
random.seed(2)
s = [i for i in range(8)]
tree = BinarySearchTree()
#若 tree = Tree(lambda x ,y : y <x) 则从大到小排
random.shuffle(s)
for x in s:
tree[x] = x #加入关键字为x，值为x的元素
print(len(tree)) #>>8
for x in tree: #首先会调用tree.__iter__()返回一个迭代器
print(f"({x[0]},{x[1]})",end = "") #从小到大遍历整个树
#>>(0,0)(1,1)(2,2)(3,3)(4,4)(5,5)(6,6)(7,7)
print()
print(3000 in tree) #>>False
print(3 in tree) #>>True
print(tree[3])                        
                        
try:
  print(tree[3000]) #关键字为3000的元素不存在，此句引发异常
except Exception as e:
  print(e) #>>key not found
tree[3000] = "ok" #添加关键字为3000，值为"ok"的元素
print(tree[3000],len(tree)) #>>ok 9
tree[3000] = "bad" #将关键字为3000的元素的值改为"bad"
print(tree[3000],len(tree)) #>>bad 9
try:
  tree.pop(354) #关键字为354的元素不存在，此句引发异常
except Exception as e:
  print(e) #>>key not found
tree.pop(3)
print(len(tree))                        
                        
                      
                 
                     
       
#复杂度：建树:O(n*log(n))      深度:log(n)
#查询、插入、查找的log(n)复杂度：（平均）
#可能退化为杆的时候会为O(n)复杂度
#
                       
     
          
          
