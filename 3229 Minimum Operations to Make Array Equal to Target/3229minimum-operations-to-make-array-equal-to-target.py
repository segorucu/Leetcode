class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        
        n = len(nums)

        incr = decr = ops = 0
        for i in range(n):
            val = target[i] - nums[i]
            if val > 0:
                if incr < val:
                    ops += val - incr
                incr = val
                decr = 0
            elif val < 0:
                if decr > val:
                    ops += (decr - val)
                decr = val
                incr = 0
            else:
                incr = decr  = 0

        return ops

            