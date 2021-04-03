n = int(input())
h = list(map(int, input().split()))
dp = [-1]*n

dp[n-1] = 0

for i in range(n-2, -1, -1):
    x = abs(h[i]-h[i+1])+dp[i+1]
    y = abs(h[i]-h[i+2])+dp[i+2] if i+2<n else int(1e9)

    dp[i] = min(x,y)

print(dp[0])
    

