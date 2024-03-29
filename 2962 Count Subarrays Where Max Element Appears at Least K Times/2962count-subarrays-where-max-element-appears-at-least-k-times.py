class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        

        mp = collections.defaultdict(int)
        maxval = max(nums)
        ans = 0
        tot = 0
        for i, num in enumerate(nums):
            if num == maxval:
                tot += 1
                mp[tot] = i
            if tot >= k:
                ans += mp[tot-k+1] + 1

        return ans
                
