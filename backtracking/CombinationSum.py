class Leetcode:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        '''
            Given an array of distinct integers candidates and a target integer target,
            return a list of all unique combinations of candidates where the chosen numbers
            sum to target. You may return the combinations in any order.
            The same number may be chosen from candidates an unlimited number of times.
            Two combinations are unique if the frequency of at least one of the chosen numbers is different.
            It is guaranteed that the number of unique combinations that sum up to target is less than 150
            combinations for the given input.
        '''
        result, temp = [], []
        cand.sort()
        
        def backtrack(have=0, start=0):
            
            if have>=target:
                if have==target:
                    result.append(deepcopy(temp))
                return
            
            for i in range(start, len(cand)):
                if(have+cand[i]> target):
                    break
                    
                temp.append(cand[i])
                backtrack(have+cand[i], i)
                temp.pop()
        
        backtrack()
        return result

    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        '''
            Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
            Each number in candidates may only be used once in the combination.
            Note: The solution set must not contain duplicate combinations.
        '''
        def backtrack(comb, remain, curr, results):
            
            if remain==0:
                results.append(list(comb))
                return
            
            for next_curr in range(curr, len(cand)):
                
                if next_curr>curr and cand[next_curr]==cand[next_curr-1]:
                    continue
                
                pick = cand[next_curr]
                
                # optimization
                if remain-pick <0:
                    break
                
                comb.append(pick)
                backtrack(comb, remain-pick, next_curr+1, results)
                comb.pop()
            
            
            
        
        cand.sort()
        comb, results = [], []
        backtrack(comb, target, 0, results)
        return results
