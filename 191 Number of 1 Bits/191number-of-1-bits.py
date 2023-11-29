class Solution:
    def hammingWeight(self, n: int) -> int:
        
        sm = 0
        while n > 0:
            sm += n % 2
            n = n // 2

        return sm


        