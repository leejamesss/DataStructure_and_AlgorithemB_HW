#queue
#push 
#pop    



class Queue:
    _initC=8
    _expandFactor=1.5
    def __init__(self):
        self._q=[None for i in range(Queue._initC)]
        self._size=0
        self.capacity=Queue._initC
#2 stack to 1 queue   instack outstack 
    def push(self,x):
        if self._size==self.capacity:
            self._expand()
        self._q[self._size]=x
        self._size+=1
    def pop(self):
        if self._size==0:
            return None
        self._size-=1
        return self._q[self._size]
    def _expand(self):
        self.capacity=int(self.capacity*Queue._expandFactor)
        tmp=[None for i in range(self.capacity)]
        for i in range(self._size):
            tmp[i]=self._q[i]
        self._q=tmp
    def __str__(self):
        return str(self._q[:self._size])
    def __repr__(self):
        return str(self._q[:self._size])
    def __len__(self):
        return self._size
    def __getitem__(self,i):
        return self._q[i]
    def __setitem__(self,i,x):
        self._q[i]=x
    def __iter__(self):
        return QueueIterator(self)
class QueueIterator:
    def __init__(self,q):
        self._q=q
        self._i=0
    def __next__(self):
        if self._i>=len(self._q):
            raise StopIteration
        self._i+=1
        return self._q[self._i-1]
    def __iter__(self):
        return self
# q=Queue()
# q.push(1)
# q.push(2)
# q.push(3)
# q.push(4)
# q.push(5)
# q.push(6)
# q.push(7)
# q.push(8)

# print(q)