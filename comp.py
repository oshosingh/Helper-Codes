from collections import defaultdict

lambda inp : input()
lambda inpS : input().split()
lambda inpI : list(map(int, inpS()))

################ Helper Data Structures ##################

class Graph:
    def __init__(self,v):
        self.dicts = defaultdict(list)
        self.V = v
        

    def addEdge(self,u,v):
        self.dicts[u].append(v)

    # -----------------Depth First Traversal------------------
    def depthFirst(self,start):
        visited = [False]*self.V
        self.depthFirstUtil(start,visited)

    def depthFirstUtil(self,start,visited):
        visited[start] = True
        print(start, end=" ")

        for i in self.dicts[start]:
            if visited[i]==False:
                self.depthFirstUtil(i, visited)

    # --------------------------------------------------------

    #------------------Breadth First Traversal ----------------            
    def breadthFirst(self,s):
        queue = []
        queue.append(s)
        visited = [False]*self.V
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=' ')

            for i in self.dicts[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

    # -----------------------------------------------------------

    # -----------------Topological Sorting ----------------------
    def topologicalSortUtil(self,v,visited,stack): 
  
        visited[v] = True
        
        for i in self.dicts[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        stack.insert(0,v) 

    def topologicalSort(self): 
        visited = [False]*self.V 
        stack =[] 
 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack)
                
        return stack
    # -----------------------------------------------------------
############################################################################    

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.leng = len(arr)
        self.tree = [0]*(2*self.leng)
        # maximum ranged queries

    def constructTree(self):
        self.tree[n:] = arr

        for i in range(n-1,0,-1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def updateTree(self, ind, val):
        ind += self.leng
        self.tree[ind] = val

        while(ind>1):
            ind = ind//2
            newVal = max(self.tree[2*ind], self.tree[2*ind+1])
            if self.tree[ind]!=newVal:
                self.tree[ind] = newVal
            else:
                break
            
    def maxQuery(self, start, end):
        # end is exclusive
        start += n
        end += n

        maxs = -1e9
        while(start<end):

            if((start &1)):   # if start is odd
                maxs = max(maxs, tree[start])
                start += 1

            if((end) & 1):  #if end is odd
                end -= 1
                maxs = max(maxs, tree[end])

            start = start//2
            end = end//2
        return maxs


################ Helper Methods ##########################
def toString(a):
    return ''.join(a)

def permute(a, l, r, ans):
    if l==r:
        ans.append(toString(a))
        return
    
    for i in range(l,r+1):
        a[l], a[i] = a[i], a[l]
        permute(a, l+1, r)
        a[l], a[i] = a[i], a[l]       #backtrack

def genAllLengthCombOfString(strs):
    contains = set()
    visited = [False]*len(strs)

    def dfs(curr):
        contains.add(curr)
        for i in range(len(strs)):
            if(not visited[i]):
                visited[i] = True
                dfs(curr + strs[i])
                visited[i] = False    #backtrack
    dfs("")
    return len(contains)-1
    # -1 for excluding empty string
                
def genAllSubsets(arr, n):
    _list = []
    for i in range((1<<n)):
        subset = ""
        for j in range(n):
            if(i & (1<<j)):
                subset += str(arr[j]) + " "
        if subset not in _list and len(subset)>0:
            _list.append(subset)
            
    final = []
    for subset in _list:
        final.append(list(map(int, subset.split())))
    
    return final
 
###########################################################



####################### Algorithms ##########################

class Kosaraju:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.V = v
        # Strongly Connected Components

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def fillOrder(self, stack, visited, v):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fillOrder(stack, visited, i)
        stack = stack.append(v)

    def getTranspose(self):
        g = Kosaraju(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def DFSUtil(self, visited, v):
        visited[v] = True
        print(v, end=' ')
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(visited, i)

    def printSCCs(self):
        stack = []
        visited = [False]*self.V

        # Fill the stack based on ascending order of vertex's finish time
        for i in range(self.V):
            if not visited[i]:
                self.fillOrder(stack, visited, i)

        print(stack)

        # Reversing the graph
        gr = self.getTranspose()

        # DFS on the reverse graph to get the components
        visited = [False]*self.V

        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.DFSutil(visited, i)
                print()
                
            
                
            
        
        





























    
    
