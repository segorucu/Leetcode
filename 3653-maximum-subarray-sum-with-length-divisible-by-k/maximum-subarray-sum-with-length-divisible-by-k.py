class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
  
        sm = 0
        modval = {0: 0}
        ans = -inf
        for i, num in enumerate(nums):
            j = i+1
            sm += num
            if j%k not in modval:
                modval[j%k] = sm
            else:
                ans = max(ans, sm - modval[j%k])
                modval[j%k] = min(modval[j%k], sm)

        return ans