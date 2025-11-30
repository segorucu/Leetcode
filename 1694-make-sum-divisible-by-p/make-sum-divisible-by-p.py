class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        target = sum(nums)
        if target < p:
            return -1
        if target % p == 0:
            return 0
        lastsum = {0: -1}

        currsm = 0
        minlen = inf
        for i, val in enumerate(nums):
            currsm += val
            currsm = currsm % p
            needed = (currsm - target + p) % p
            if needed in lastsum:
                minlen = min(minlen, i-lastsum[needed])

            lastsum[currsm] = i

        if minlen >= len(nums):
            return -1
        return minlen
