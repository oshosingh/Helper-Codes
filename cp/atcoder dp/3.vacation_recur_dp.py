import sys
sys.setrecursionlimit(10**5+7)

n = int(input())

days = []
for i in range(n):
    x = list(map(int, input().split()))
    days.append(x)

def fun(idx, chosen, days, n,dp):
    if idx==n-1:
        if chosen==0:
            return max(days[n-1][1], days[n-1][2])
        elif chosen==1:
            return max(days[n-1][0], days[n-1][2])
        else:
            return max(days[n-1][0], days[n-1][1])

    if dp[idx][chosen]!=-1:
        return dp[idx][chosen]
    
    if chosen==0:
        dp[idx][chosen] = days[idx][chosen]+ max(fun(idx+1,1,days,n,dp), fun(idx+1,2,days,n,dp))
        return dp[idx][chosen]
    elif chosen==1:
        dp[idx][chosen] = days[idx][chosen]+ max(fun(idx+1,0,days,n,dp), fun(idx+1,2,days,n,dp))
        return dp[idx][chosen]
    else:
        dp[idx][chosen] = days[idx][chosen]+ max(fun(idx+1,0,days,n,dp), fun(idx+1,1,days,n,dp))
        return dp[idx][chosen]

ans = 0
dp = [[-1]*3 for _ in range(n)]
for i in range(3):
    ans = max(ans, fun(0,i,days,n,dp))

print(ans)
    
    
