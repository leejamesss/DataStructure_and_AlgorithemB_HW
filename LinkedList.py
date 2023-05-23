class LinkedList:
    class Node:
        def __init__(self,data,next=None):
            self.data,self.next=data,next
    def __init__(self):
        self.head=self.tail=None
        self.size=0
    def printList(self):
        ptr=self.head
        while ptr is not None:
            print(ptr.data,end=',')
            ptr=ptr.next
    def insert(self,p,data):
        nd=LinkedList.Node(data,None)
        if self.tail is p:
            self.tail=nd
        nd.next=p.next
        p.next=nd
        self.size+=1
    def delete(self,p):
        if self.tail is p.next:
            self.tail=p
        p.next=p.next.next
        self.size-=1
    def popFront(self):
        if self.head is None:
               raise \
          Exception("Poping front for Empty List")
        else:
            self.head=self.head.next
            self.size-=1
            if self.size is 0:
                self.head=self.tail=None
    def pushBack(self,data):
        if self.size==0:
            self.pushFront(data)
        else:
            self.insert(self.tail,data)
    def pushFront(self,data):
        nd=LinkedList.Node(data,None)
        self.head=nd
        self.size+=1
        if self.tail is None:
            self.tail=nd
    def clear(self):
        self.head=self.tail=None
        self.size=0
    def __len__(self):
        return self.size
    def __iter__(self):
        self.ptr=self.head
        return self
    def __next__(self):
        if self.ptr is None:
            raise StopIteration()
        else:
            data=self.ptr.data
            self.ptr=self.ptr.next
            return data
    def __str__(self):
        return str([x for x in self])
    def __repr__(self):
        return str(self)
    def __getitem__(self,index):
        if index<0 or index>=self.size:
            raise IndexError()
        else:
            ptr=self.head
            for i in range(index):
                ptr=ptr.next
            return ptr.data
    def __setitem__(self,index,data):
        if index<0 or index>=self.size:
            raise IndexError()
        else:
            ptr=self.head
            for i in range(index):
                ptr=ptr.next
            ptr.data=data
    def __delitem__(self,index):
        if index<0 or index>=self.size:
            raise IndexError()
        else:
            ptr=self.head
            for i in range(index-1):
                ptr=ptr.next
            self.delete(ptr)
    def __contains__(self,data):
        ptr=self.head
        while ptr is not None:
            if ptr.data==data:
                return True
            ptr=ptr.next
        return False
    def __add__(self,other):
        new=LinkedList()
        for x in self:
            new.pushBack(x)
        for x in other:
            new.pushBack(x)
        return new
    def __iadd__(self,other):
        for x in other:
            self.pushBack(x)
        return self
    def __mul__(self,other):
        new=LinkedList()
        for x in self:
            for i in range(other):
                new.pushBack(x)
        return new
    def __imul__(self,other):
        for x in self:
            for i in range(other-1):
                self.pushBack(x)
        return self
    def __eq__(self,other):
        if self.size!=other.size:
            return False
        else:
            ptr1,ptr2=self.head,other.head
            while ptr1 is not None:
                if ptr1.data!=ptr2.data:
                    return False
                ptr1,ptr2=ptr1.next,ptr2.next
            return True
    def __ne__(self,other):
        return not self==other
    def __lt__(self,other):
        ptr1,ptr2=self.head,other.head
        while ptr1 is not None and ptr2 is not None:
            if ptr1.data<ptr2.data:
                return True
            elif ptr1.data>ptr2.data:
                return False
            ptr1,ptr2=ptr1.next,ptr2.next
        return self.size<other.size
    def __le__(self,other):
        return self<other or self==other
    def __gt__(self,other):
        return not self<=other
    