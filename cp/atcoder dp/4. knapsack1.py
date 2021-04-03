import sys
sys.setrecursionlimit(10**5+7)

def recur(i,wleft):
    if wleft<0:
        return -1*int(1e18)
    if i==n:
        return 0
    if dp[i][wleft]!=-1:
        return dp[i][wleft]

    dp[i][wleft] = max(recur(i+1, wleft),val[i]+ recur(i+1, wleft-wt[i]) )
    return dp[i][wleft]
    

n, w = map(int, input().split())
wt = [0]*w
val = [0]*w

for i in range(n):
    wt[i], val[i] = map(int, input().split())

dp = [[-1]*(100100) for _ in range(101)]
print(recur(0,w))

# in recur( 0 -> bag is empty, w -> knapsack weight)
