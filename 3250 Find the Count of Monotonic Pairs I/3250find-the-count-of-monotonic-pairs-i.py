from functools import cache
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        MOD = 10**9+7
        arr2 = n*[0]

        @cache
        def dp(i, start):
            if i == n:
                return 1
            
            ans = 0
            for a1 in range(start,nums[i]+1):
                a2 = nums[i] - a1
                if a2 < 0:
                    break
                if i > 0 and a2 > arr2[i-1]:
                    continue
                arr2[i] = a2
                ans += dp(i+1, max(a1,nums[i]-a2))
            return ans % MOD
        return dp(0, 0)