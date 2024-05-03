class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        mask = k
        for num in nums:
            mask ^= num

        ans = 0
        while mask > 0:
            ans += (mask & 1)
            mask = mask >> 1


        return ans