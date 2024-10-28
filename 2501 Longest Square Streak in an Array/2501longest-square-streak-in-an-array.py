class Solution:
    from sortedcontainers import SortedSet
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        numsset = set(nums)
        nums = sorted(list(nums),reverse=True)

        ans = -1
        while nums:
            curr = nums.pop()
            size = 0
            while curr in numsset:
                numsset.remove(curr)
                size += 1
                curr = curr ** 2
            ans = max(size, ans)
        
        return ans if ans > 1 else -1


