class KadaneAlgo:
    # Largest sum contiguous subarray
    
    def kadanes(self, arr) -> list:
        '''
            Returns [maxSum, [start idx, end idx of subarray]]
        '''
        n = len(arr)
        maxSoFar = -1*int(1e9)
        maxEndingHere = 0

        start = 0
        end = 0
        s = 0

        for i in range(n):
            maxEndingHere += arr[i]

            if maxEndingHere>maxSoFar:
                maxSoFar = maxEndingHere
                start = s
                end = i

            if maxEndingHere<0:
                maxEndingHere = 0
                s = i+1

        return [maxSoFar, [start, end]]

class GeneralDP:
    def __init__(self):
        
    def lbs(self, arr):
        '''
        Given an array containing n positive integers, a subsequence is called
        bitonic if it is first increasing and the decreasing
        '''
        n = len(arr)
        
        # longest increasing subsequence
        lis = [1]*n

        for i in range(1, n):
            for j in range(0, i):
                if(arr[i]>arr[j] and lis[i]<lis[j]+1):
                    lis[i] = lis[j]+1

        # longest decreasing subsequence
        lds = [1]*n

        for i in reversed(range(n-1)):
            for j in reversed(range(i-1, n)):
                if arr[i]>arr[j] and lds[i]<lds[j]+1:
                    lds[i] = lds[j]+1

        maxim = lis[0]+lds[0]-1
        for i in range(1,n):
            maxim = max(maxim, lis[i]+lds[i]-1)

        return maxim
