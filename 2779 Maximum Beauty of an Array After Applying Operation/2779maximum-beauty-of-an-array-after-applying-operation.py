class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        if n == 1:
            return 1

        count = 0
        l = r = 0
        while r < n:
            while nums[r]-nums[l] > 2 * k:
                l += 1
            r += 1
            count = max(count, r-l)

        return count 