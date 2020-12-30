from Interfaces import List
import numpy as np

class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        '''
            Get the i-th node in the list
        '''
        if i < self.n/2:
            p = self.dummy.next
            for z in range(i):
                p = p.next
        else:
            p = self.dummy
            for z in range(self.n - i):
                p = p.prev
        return p

    def get(self, i) -> np.object:
        if i < 0 or i >= self.n:
            raise IndexError('Index out of bounds...')
        return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
        if i < 0 or i >= self.n:
            raise IndexError('Index out of bounds...')
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w : Node, x : np.object) -> Node:
        if w is None:
            raise Exception("Node is currently Null...")
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u
            
    def add(self, i : int, x : np.object)  :
        # Check preconditions
        # if i < 0 or i >= self.n:
        #     raise IndexError("Index out of bounds...")
        # find i'th node and insert x right before it
        self.add_before(self.get_node(i), x)

    def _remove(self, w : Node) :
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
    
    def remove(self, i :int) :
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds...")
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        for i in range(0, self.n):
            if self.get(i) != self.get(self.n-i-1):
                return False
        return True

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
