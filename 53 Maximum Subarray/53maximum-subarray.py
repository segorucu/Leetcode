class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        sm = 0
        ans = -float("inf")
        for right in range(len(nums)):
            sm += nums[right]
            ans = max(ans,sm)
            while sm < 0 and left <= right:
                sm -= nums[left]
                left += 1
        return ans

        