from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.V = v
        self.dicts = defaultdict(list)

    def addEdge(self, u, v):
        self.dicts[u].append(v)

    def dfs(self, start):
        visited = [False]*self.V
        self.__dfsUtil(start, visited)

    def __dfsUtil(self, start, visited):
        visited[start] = True
        print(start, end=" ")
        for i in self.dicts[start]:
            if visited[i]==False:
                self.dfsUtil(i, visited)

    def bfs(self, s):
        queue = []
        queue.append(s)
        visited = [False]*self.V
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.dicts[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.__sortUtil(i,visited,stack)
        return stack

    def __sortUtil(self,v,visited,stack):
        visited[v] = True
        for i in self.dicts[v]:
            if not visited[i]:
                self.sortUtil(i,visited,stack)
        stack.insert(0,v)
            
        
        
        
