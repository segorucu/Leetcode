class Solution:

    def isPrime(self,n):
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def isUgly(self, n: int) -> bool:

        if n < 1:
            return False
        
        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5
        if n == 1:
            return True

        return False
        