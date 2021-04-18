'''
You are given a tree with n nodes numbered from 0 to n-1 in the form of a
parent array where parent[i] is the parent of node i. The root of the tree
is node 0.Implement the function getKthAncestor(int node, int k) to return
the k-th ancestor of the given node. If there is no such ancestor, return -1.
The k-th ancestor of a tree node is the k-th node in the path from that node
to the root.

Leetcode -> 1483: Kth Ancestor of Tree Node
'''

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.log = 0

        while(1<<self.log< n):
            self.log += 1

        self.up = [[0]*self.log for _ in range(n)]
        self.depth = [0]*n

        parent[0] = 0

        for v in range(n):
            self.up[v][0] = parent[v]

            if v!=0:
                self.depth[v] = self.depth[parent[v]]+1

            for j in range(1, self.log):
                self.up[v][j] = self.up[self.up[v][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int)-> int:
        # no ancestor above
        if(self.depth[node]<k):
            return -1

        for j in range(self.log-1, -1, -1):
            if(k>= (1<<j)):
                node = self.up[node][j]
                k -= 1<<j
        return node
        
