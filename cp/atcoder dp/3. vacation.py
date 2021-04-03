n = int(input())
dp = [0]*3

for day in range(n):
    c = list(map(int, input().split()))
    new_dp = [0]*3

    for i in range(3):
        for j in range(3):
            if i!=j:
                new_dp[j] = max(new_dp[j],dp[i]+c[j])

    dp = new_dp

print(max(dp[0], dp[1], dp[2]))
        
                
        
    
    
