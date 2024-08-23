class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        r = 0
        n = len(nums)
        odds = 0
        l = 0
        ans = 0
        while r < n:
            if nums[r] % 2 == 1:
                odds += 1

            while r < n and odds > k:
                if nums[l] % 2 == 1:
                    odds -= 1
                l += 1

            if odds == k:
                p = l
                while nums[p] % 2 != 1:
                    p += 1
                ans += p-l+1
            
            r += 1

        return ans