
class StringOpr:
    def __init__(self):

    def longestPalindrome(self, s: str) -> str:
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
            
	    # j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):
                
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)

                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom

    def longestCommonSubstring(self, x, y, state=False):
        m = len(x)
        n = len(y)
        dp = [[0]*(n+1) for _ in range(m+1)]

        '''
            Time Complexity -> O(n*m)
            Space Complexity -> O(n*m)
        '''
        length = 0; result = 0
        row, col = 0, 0

        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j] = 0
                elif x[i-1] == y[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    result = max(result, dp[i][j])
                    if state and length<dp[i][j]:
                        length = dp[i][j]
                        row = i
                        col = j
                    else:
                        dp[i][j] = 0
        if state:
            result = ['0']*length

            while dp[row][col]!=0:
                length -= 1
                result[length] = x[row-1]
                row -= 1
                col -= 1
            return ''.join(result)
        else:
            return result

    def __lcsOptim(self, x, y):
        m = len(x)
        n = len(y)

        '''
            Time Complexity - O(n*m)
            Space Complexity - O(2*n)
        '''

        result = 0
        end = 0 # To store ending point of lcs

        length = [[0]*m for _ in range(2)]

        currRow = 0

        for i in range(m+1):
            for j in range(n+1):
                if(i==0 or j==0):
                    length[currRow][j] = 0
                elif x[i-1]==y[j-1]:
                    length[currRow][j] = length[1-currRow][j-1]+1

                    if length[currRow][j]>result:
                        result = length[currRow][j]
                        end = i-1
                else:
                    length[currRow][j] = 0
            currRow = 1-currRow

        if result==0:
            return -1
        return x[end-result+1:end+1]


    def longestCommonSubsequence(self, x, y, state=False):
        m = len(x)
        n = len(y)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if(i==0 or j==0):
                    dp[i][j] = 0
                elif x[i-1]==y[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        if state:
            index = dp[m][n]
            lcs = [""]*(index+1)
            lcs[index] = ""

            i = m
            j = n
            while i>0 and j>0:
                if x[i-1]==y[j-1]:
                    lcs[index-1] = x[i-1]:
                        i -= 1; j-=1; index-=1
                elif dp[i-1][j]>dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
                    
            return "".join(lcs)
        return dp[m][n]
        
            
        

        
                    
                
                    
                
            
        
        
                
        
        

    
        
