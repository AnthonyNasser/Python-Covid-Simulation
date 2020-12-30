from Interfaces import Graph, List
import numpy as np
import ArrayList
import SLLQueue
import ArrayStack

class AdjacencyMatrix(Graph):
    def __init__(self, n : int):
        self.n = n
        self.a = self.new_boolean_matrix(self.n)

    def new_boolean_matrix(self, n):
        return np.zeros([n, n], np.bool_)

    def new_boolean_array(self, n):
        return np.zeros(n, np.bool_)

    def add_edge(self, i : int, j : int):
        self.a[i][j] = True

    def remove_edge(self, i : int, j : int):
        try:
            self.a[i][j] = False
        except IndexError:
            return None

    def has_edge(self, i : int, j: int) -> bool:
        try:
            return self.a[i][j]
        except IndexError:
            return None

    def out_edges(self, i) -> List:
        l = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(i, j):
                l.append(j)
        return l

    def in_edges(self, j) -> List:
        l = ArrayList.ArrayList()
        for i in range(self.n):
            if self.has_edge(i, j):
                l.append(i)
        return l

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
                    print(f"{i} and {j} are in a cycle...")

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.a[i].__str__())
        return s
