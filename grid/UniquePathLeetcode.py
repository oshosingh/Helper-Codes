class UniquePath:
    # 1
    def uniquePaths(self, m: int, n: int) -> int:
        # m- row and n- col
        if m==1 and n>0:
            return 1
        if m>0 and n==1:
            return 1
        dp = [[0]*n for _ in range(m)]
        dp[-1][-1] = 0
        
        dp[-1][-2] = 1
        dp[-2][-1] = 1
        
        # last row
        for i in range(n-3, -1, -1):
            dp[-1][i] = dp[-1][i+1]
        
        # last col
        for i in range(m-3, -1, -1):
            dp[i][-1] = dp[i+1][-1]
        
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j]+ dp[i][j+1]
        
        return dp[0][0]

    # 2
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid) # row
        n = len(grid[0]) # col
        
        dp = [[0]*n for _ in range(m)]

        # Base cases
        if m==1 and n==1 and grid[0][0]==0:
            return 1
        
        if m==1 and n==1 and grid[0][0]==1:
            return 0
        
        if grid[-1][-1]==1 or grid[0][0]==1:
            return 0
        
        grid[-1][-1] = 0
        
        # last row
        for i in range(n-2, -1, -1):
            if grid[-1][i] == 1:
                dp[-1][i] = -1
            else:
                if i==n-2:
                    dp[-1][i] = 1
                else:
                    dp[-1][i] = dp[-1][i+1]
        
        # last col
        for i in range(m-2, -1, -1):
            if grid[i][-1] == 1:
                dp[i][-1] = -1
            else:
                if i==m-2:
                    dp[i][-1] = 1
                else:
                    dp[i][-1] = dp[i+1][-1]
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if grid[i][j] != 1:
                    if dp[i+1][j] != -1:
                        dp[i][j] += dp[i+1][j]
                    if dp[i][j+1] != -1:
                        dp[i][j] += dp[i][j+1]

        return dp[0][0]
