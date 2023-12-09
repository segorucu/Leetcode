class Solution:
    def reverse(self, x: int) -> int:
        
        positive = True
        if x < 0:
            positive = False
        x = abs(x)
        ans = 0
        while x > 0:
            rem = x % 10
            x = x // 10
            ans = 10*ans + rem
            
        if not positive:
            ans *= -1

        if ans < -2**31 or ans > 2**31-1:
            return 0 
        return ans