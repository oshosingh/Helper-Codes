
class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0]*(2*self.leng)
        # maximum ranged queries

    def constructMaxTree(self):
        self.tree[self.n:] = self.arr

        for i in range(n-1,0,-1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def updateMaxTree(self, ind, val):
        ind += self.n
        self.tree[ind] = val

        while ind>1:
            ind = ind//2
            newVal = max(self.tree[2*ind], self.tree[2*ind+1])
            if self.tree[ind]!=newVal:
                self.tree[ind] = newVal
            else:
                break
            
    def maxQuery(self, start, end):
        # end not included
        start += self.n
        end += self.n
        maxs = -1*int(1e9)
        while start<end:
            if((start&1)):
                maxs = max(maxs, tree[start])
                start += 1

            if((end)&1):
                end -= 1
                maxs = max(maxs, tree[end])
            start = start//2
            end = end//2
        return maxs
                
        
