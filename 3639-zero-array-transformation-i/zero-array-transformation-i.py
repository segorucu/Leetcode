class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        n = len(nums)
        increment = n * [0]
        for l,r in queries:
            increment[l] -= 1
            if r+1 < n:
                increment[r+1] += 1

        for i in range(n):
            if i > 0:
                increment[i] += increment[i-1]
            nums[i] += increment[i]
            if nums[i] > 0 :
                return False

        return True