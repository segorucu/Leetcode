class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        modval = {}
        ans = -inf
        for i, val in enumerate(prefix):
            if i%k not in modval:
                modval[i%k] = val
            else:
                ans = max(ans, val - modval[i%k])
                modval[i%k] = min(modval[i%k], val)

        return ans