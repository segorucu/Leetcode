class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
  
        nums = [0] + nums
        sm = 0
        modval = {}
        ans = -inf
        for i, num in enumerate(nums):
            sm += num
            if i%k not in modval:
                modval[i%k] = sm
            else:
                ans = max(ans, sm - modval[i%k])
                modval[i%k] = min(modval[i%k], sm)

        return ans