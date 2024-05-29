class Solution:
    def numSteps(self, s: str) -> int:
        
        num = 0
        for i, val in enumerate(s):
            num = num * 2 + int(val)

        count = 0
        while num != 1:
            if num & 1 == 1:
                num += 1
                count += 1
            else:
                num >>= 1
                count += 1
                
        return count