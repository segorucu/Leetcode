from functools import cache
class Solution:
    def maxScore(self, nums: List[int]) -> int:

        n = len(nums)

        @cache 
        def dp(mask,op):
            if op == n//2+1:
                return 0

            ret = 0
            for i in range(n):
                for j in range(i+1,n):
                    if ((mask & (1<<i)) | (mask & (1<<j))):
                        continue
                    score = math.gcd(nums[i],nums[j])
                    oldmask = mask
                    mask = mask | (1 << i) | (1 << j)
                    ret = max(ret,dp(mask,op+1) + op*score)
                    mask = oldmask
            return ret

        return dp(0,1)