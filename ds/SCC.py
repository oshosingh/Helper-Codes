from collections import defaultdict

class Kosaraju:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.V = v

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, stack, visited, v):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                dfs(stack,visited,i)
                
        # Fill the stack based on ascending order of vertex's finish time
        stack.append(v)

    def getTranspose(self):
        g = Kosaraju(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def dfsUtil(self, visited, v, comp):
        visited[v] = True
        print(v, end = " ")
        comp.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfsUtil(visited, i)

    def getSCC(self) -> list:
        visited = [False]*self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                dfs(stack,visited,i)

        # Reversing the Graph
        gr = self.getTranspose()

        # DFS on the reverse graph to get the components
        visited = [False]*self.V
        components = []

        while stack:
            i = stack.pop()
            comp = []
            if not visited[i]:
                gr.dfsUtil(visited, i, comp)
                print()
                components.append(comp)
        return components
                
        
        
