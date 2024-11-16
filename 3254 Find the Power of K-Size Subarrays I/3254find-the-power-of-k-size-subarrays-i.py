class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        if n == 1:
            return nums

        ans = []
        l, r = 0, 0
        while r < n:
            if r > 0 and nums[r] != nums[r-1] + 1:
                l = r
            if r >= k-1:
                if r-l >= k-1:
                    ans.append(nums[r])
                else:
                    ans.append(-1)
            r += 1


        return ans