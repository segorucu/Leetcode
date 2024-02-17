from functools import cache
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        n = len(nums)

        # counter = collections.Counter(nums)
        # if len(counter.keys()) == 1:
        #     return n // 2
        # del counter
        
        @cache
        def backtrack(l,r,prev):
            if r - l < 1:
                return 0
            
            count = 0
            if nums[l] + nums[l+1] == prev:
                count = max(count,backtrack(l+2, r, prev)+1)
            if nums[l] + nums[r] == prev:
                count = max(count,backtrack(l+1, r-1, prev)+1)
            if nums[r] + nums[r-1] == prev:
                count = max(count,backtrack(l, r-2, prev)+1)

            
            return count
            
#         opt = -1: left 0: edges 1: right
        l = backtrack(0, n-1, nums[0]+nums[1])
        m = backtrack(0, n-1, nums[0]+nums[n-1])
        r = backtrack(0, n-1, nums[n-2]+nums[n-1])
                
        return max(l,m,r)
                
            