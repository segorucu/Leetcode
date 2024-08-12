class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        r = 1
        n = len(nums)
        ans = 0
        count = 0
        while r < n:
            if count % 2 == 0 and nums[r] == nums[r-1] + 1:
                count += 1
                r += 1
            elif count % 2 == 1 and nums[r] == nums[r-1] - 1:
                count += 1
                r += 1
            else:
                if count == 0:
                    r += 1
                count = 0
            ans = max(ans,count+1)
        if ans == 1:
            return -1
        return ans
            


        