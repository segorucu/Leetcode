import math
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        nums.sort()
        left = 1
        right = max(nums)
        n = len(nums)

        def calculatenumberofoperations(maxballsize):
            p = n-1
            ops = 0
            while p >= 0 and nums[p] > maxballsize:
                ops += math.ceil(nums[p]/maxballsize)-1
                p -= 1
            return ops


        while left < right:
            mid = (left+right) // 2
            ops = calculatenumberofoperations(mid)
            if ops > maxOperations:
                left = mid+1
            else:
                right = mid

        return left