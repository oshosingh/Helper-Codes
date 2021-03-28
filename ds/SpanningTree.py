class Krushkal:

    '''
        Return [cost,list of edges in spanning tree]
    '''
    def __init__(self, v, mintree = True):
        self.graph = []
        self.V = v
        self.mintree = mintree


    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])

    # find parent method
    def find(self, parent, x):
        if parent[x]== -1:
            return x
        return self.find(parent, parent[x])

    # union method for joining the set
    def union(self, parent, x, y):
        xp = self.find(parent, x)
        yp = self.find(parent, y)

        if xp!=yp:
            parent[yp] = xp

    def krushkalMST(self):
        result = []
        i = 0 # index variable, used for sorted edges
        e = 0 # index variable used for result[]

        # sorting the edges for Minimum or Maximum spanning tree
        if self.mintree:
            self.graph = sorted(self.graph,
                                key = lambda x: x[2])
        else:
            self.graph = sorted(self.graph,
                                key = lambda x: x[2], reverse=True)

        # disjoint set initialization
        parent = [-1]*self.V

        while e< self.V-1:
            u,v,w = self.graph[i]
            i = i+1

            up = self.find(parent, u)
            vp = self.find(parent, v)

            # if cycle is not formed, include in the result
            if up!=vp:
                result.append([u,v,w])
                e = e+1
                self.union(parent, u, v)
                
            # Else discard the Edge

        cost = 0
        for u,v,w in result:
            cost += w

        return [cost, result]
        
    
