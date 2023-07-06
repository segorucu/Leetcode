class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ans = float("inf")
        left = right = 0
        sm = 0
        for right in range(len(nums)):
            sm += nums[right]
            if sm >= target:
                ans = min(ans,right-left+1)
            while left <= right and sm >= target:
                ans = min(ans,right-left+1)
                sm -= nums[left]
                left += 1

        if ans == float("inf"):
            return 0
                
        return ans
