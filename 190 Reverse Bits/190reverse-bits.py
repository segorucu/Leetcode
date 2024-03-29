class Solution:
    def reverseBits(self, n: int) -> int:
        
        rev = 0
        for i in range(32):
            rem = n & 1
            rev += (rem << 31 - i)
            n = n >> 1



        return rev