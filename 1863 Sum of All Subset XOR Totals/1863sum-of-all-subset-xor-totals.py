class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        

        def backtrack(i,curr):
            if i == len(nums):
                return curr

            one = backtrack(i+1,curr)
            curr ^= nums[i]
            two = backtrack(i+1,curr)
            return one + two


        return backtrack(0,0)