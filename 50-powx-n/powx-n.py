class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            if n % 2 == 0:
                return self.myPow(x*x,n//2)
            else:
                return self.myPow(x*x,n//2)*x
        if n < 0:
            return 1/self.myPow(x,-n)
        