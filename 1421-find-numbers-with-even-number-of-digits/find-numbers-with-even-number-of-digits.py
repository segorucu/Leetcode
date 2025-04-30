class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            digit = 0
            while num:
                num = num // 10
                digit += 1
            if digit % 2 == 0:
                count += 1
        return count