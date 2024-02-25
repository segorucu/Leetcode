class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0

        isprime = n * [1]
        isprime[0] = -1
        isprime[1] = -1
        for i in range(2,ceil(math.sqrt(n))):
            if isprime[i] == 1:
                f = 2*i
                while f < n:
                    isprime[f] = 0
                    f += i

        return isprime.count(1)