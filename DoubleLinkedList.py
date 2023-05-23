class DoubleLinkedList:
    class _Node:
        def __init__(self,data,prev=None,next=None):
            self.data,self.prev,self.next=data,prev,next
    class _Iterator:
        def __init__(self,p):
            self._ptr=p
        def getData(self):
            return self._ptr.data
        def setData(self,data):
            self._ptr.data=data
        
        def __next__(self):
            self._ptr=self._ptr.next
            if self._ptr is None:
                return None
            else:
                return DoubleLinkedList._Iterator(self._ptr)
        def prev(self):
            self._ptr=self._ptr.prev
            return DoubleLinkedList._Iterator(self._ptr)
    def __init__(self):
        self._head=self._tail=\
            DoubleLinkedList._Node(None,None,None)
        self._size=0
    def _insert(self,p,data):
        nd=DoubleLinkedList._Node(data,p,p.next)
        if self._tail is p:
            self._tail=nd
        if p.next:
            p.next.prev=nd
        p.next=nd
        self._size+=1
    def _delete(self,p):
        if self._size==0 or p is self._head:
            raise Exception('Illegal deleting')
        else:
            p.prev.next=p.next
            if p.next:
                p.next.prev=p.prev
            if self._tail is p:
                self._tail=p.prev
            self._size-=1
    

        return DoubleLinkedList._Iterator(newNode)

