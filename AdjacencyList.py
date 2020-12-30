"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue
import SLLQueue
import pdb

class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def new_boolean_matrix(self, n):
        return np.zeros([n, n], np.bool_)

    def new_boolean_array(self, n):
        return np.zeros(n, np.bool_)
            
    def add_edge(self, i, j):
        self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        for k in range(len(self.adj)):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return

    def has_edge(self, i : int, j: int) -> bool:
        try:
            for k in self.adj[i]:
                if k == j:
                    return True
            return False
        except Exception:
            return False
        
    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        out = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(j, i):
                out.append(j)
        return out
    
    def bfs(self,r : int):
        seen = self.new_boolean_array(self.n)
        q = SLLQueue.SLLQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            print(i, end = " ")
            for j in self.out_edges(i):
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True

    def bfs2(self, r: int, k: int):
        d = 0
        seen = self.new_boolean_array(self.n)
        q = SLLQueue.SLLQueue()
        q.add(r)
        seen[r] = True
        idx = []
        while q.size() > 0 and d < k:
            d += 1
            i = q.remove()
            if i not in idx:
                idx.append(i)
            for j in self.out_edges(i):
                if seen[j] == False:
                    if j not in idx:
                        idx.append(j)
                    q.add(j)
                    seen[j] = True
        return idx

    def dfs(self, r : int):
        seen = self.new_boolean_array(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        while s.size() > 0:
            i = s.pop()
            print(i, end = " ")
            seen[i] = True
            ngh = self.out_edges(i)
            for j in range(ngh.size()):
                if seen[ngh.get(j)] == False:
                    s.push(ngh.get(j))
                else:
                    continue
                    print(f"({i} and {j} are in a cycle)")

    def dfs2(self, r1 : int, r2 : int):
        d = np.zeros(self.n)
        d[r1] = 0
        seen = self.new_boolean_array(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r1)
        while s.size() > 0:
            i = s.pop()
            seen[i] = True
            ngh = self.out_edges(i)
            for k in range(len(ngh)):
                j = ngh[k]
                if seen[j] == False:
                    s.push(j)
                    d[j] = d[i] + 1
                    if j == r2:
                        return d[j]
        return -1

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s




