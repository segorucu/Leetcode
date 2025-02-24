class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        n = len(nums)
        l = r = 0
        zeros = 0
        ans = 0
        while r < n:
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            r += 1
            ans = max(ans, r-l)

        return ans
            