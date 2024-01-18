class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        prepre = 1
        pre = 2
        for i in range(3,n+1):
            dum = prepre + pre
            prepre = pre
            pre = dum
        return dum