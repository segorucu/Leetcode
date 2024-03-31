class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        
        curr = x
        sm = 0
        while curr > 0:
            sm += curr % 10
            curr = curr // 10
            
        if x % sm == 0:
            return sm
        else:
            return -1
            