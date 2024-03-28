class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        counter = collections.defaultdict(int)
        l = r = 0
        n = len(nums)
        ans = 0
        while r < n:
            counter[nums[r]] += 1
            while counter[nums[r]] > k:
                counter[nums[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
            r += 1

        return ans