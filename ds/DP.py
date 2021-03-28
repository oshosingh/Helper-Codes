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


