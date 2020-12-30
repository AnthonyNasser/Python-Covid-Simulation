from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
   
    def push(self, x : np.object) :
        try:
            # Create a new node with x and push it to the LL
            u = self.Node(x)
            u.next = self.head
            self.head = u
            if self.n == 0:
                self.tail = u
            self.n += 1
            return x
        except Exception:
            print('...')
        
    def pop(self) -> np.object:
        try:
            if self.n == 0:
                return None
            # remove the head
            x = self.head.x
            self.head = self.head.next
            self.n -= 1
            if self.n == 0:
                self.tail = None
            return x
        except Exception:
            print('...')

    def size(self) -> int:
        return self.n

    def reverse(self):
        previous_node = None
        current_node = self.head
        while (current_node is not None):
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x




