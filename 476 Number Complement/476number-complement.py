class Solution:
    def findComplement(self, num: int) -> int:
        
        ans = num
        shift = 0
        while num > 0:
            ans = ans ^ (1 << shift)
            num = num >> 1
            shift += 1
        return ans
            
