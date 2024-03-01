class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        counter = collections.Counter(s)
        return (counter['1']-1) *'1' + counter['0'] * '0' + '1'