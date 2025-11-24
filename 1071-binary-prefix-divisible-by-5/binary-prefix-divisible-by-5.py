class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        curr = 0
        ans = len(nums) * [False]
        for i, num in enumerate(nums):
            curr = curr << 1 
            curr += num
            if curr % 5 == 0:
                ans[i] = True

        return ans
