class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        N = len(nums)
        T = len(queries)

        def good(k):
            diff = (N+1) * [0]
            for l,r,v in queries[0:k]:
                diff[l] += v
                diff[r+1] -= v
            current = 0
            for i,num in enumerate(nums):
                current += diff[i]
                if num > current:
                    return False

            return True

        l = 0
        r = T+1
        while l < r:
            mid = (l+r) // 2
            if good(mid):
                r = mid
            else:
                l = mid + 1

        if l == T+1:
            return -1
        return l

