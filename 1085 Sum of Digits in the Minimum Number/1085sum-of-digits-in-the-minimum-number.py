class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        val = min(nums)
        sm = 0
        while val > 0:
            sm += val % 10
            val = val // 10
        if sm % 2 == 0:
            return 1
        else:
            return 0


        