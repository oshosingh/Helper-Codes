class LeetcodeUniquePathIII:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        start = [0, 0]
        ans = 0
        num_zero = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    start[0], start[1] = i, j
                
                if grid[i][j]==0:
                    num_zero += 1
        
        
        def backtrack(x, y, num_zero):
            nonlocal ans
            nonlocal r
            nonlocal c
            
            move = [[0,1], [0,-1],[1,0],[-1,0]]
            
            temp = grid[x][y]
            
            # make the grid not reachable
            grid[x][y] = "#"
            
            for delta_x, delta_y in move:
                new_x = x+ delta_x
                new_y = y+ delta_y
                
                if 0<=new_x<r and 0<=new_y<c:
                    if grid[new_x][new_y]==2 and num_zero==0:
                        ans += 1
                    elif grid[new_x][new_y]==0:
                        new_num_zero = num_zero-1
                        backtrack(new_x, new_y, new_num_zero)
            
            grid[x][y] = temp              
            
        
        backtrack(start[0], start[1], num_zero)
        return ans
        
                
            
                    
        
