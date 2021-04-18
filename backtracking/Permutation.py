from collections import Counter

class Permutation:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Generating all possible permutations
        result = []

        def backtrack(nums, l, r):
            if l==r:
                result.append(deepcopy(nums))
                return

            for i in range(l, r+1):
                nums[l], nums[i] = nums[i], nums[l]
                backtrack(nums, l+1, r)
                nums[l], nums[i] = nums[i], nums[l]

        backtrack(nums, 0, len(nums)=1)
        return result

    def uniquePermute(self, nums: List[int]) -> List[List[int]]:
        '''
            Given a collection of numbers, nums, that might contain duplicates,
            return all possible unique permutations in any order.
        '''

        result = []

        def backtrack(temp, counter):
            if len(temp)==len(nums):
                nums.append(list(temp))
                return

            for num in counter:
                if counter[num]>0:
                    temp.append(nums)
                    counter[num] -= 1

                    backtrack(temp, counter)

                    temp.pop()
                    counter[num] += 1
                
        backtrack([], Counter(nums))
        return result
