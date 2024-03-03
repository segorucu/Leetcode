class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        prod = 1
        i = 0
        n = len(nums)
        while i < n and nums[i] == 0:
            i += 1
        if i == n:
            return 0
        i += 1
        while i < n:
            count = 0
            while i < n and nums[i] == 0:
                count += 1
                i += 1
            if i == n:
                break
            count += 1
            prod = (prod * count) % MOD
            i += 1
        return prod