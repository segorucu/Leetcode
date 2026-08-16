class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        

        curr = 0
        zeros = 0
        n= len(nums)
        for i, num in enumerate(nums):
            curr ^= num
            if num == 0:
                zeros += 1
        if curr != 0:
            return n
        if zeros == n:
            return 0

        return n-1
