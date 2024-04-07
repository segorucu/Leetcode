class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        count = 0
        l = r = 0
        n = len(nums)
        sm = 0
        for r in range(n):
            num = nums[r]
            sm += num
            prod = sm * (r-l+1)
            while prod >= k:
                sm -= nums[l]
                l += 1
                prod = sm * (r-l+1)
            count += (r-l+1)


        return count