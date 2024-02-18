import math
class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        
        
        def is_prime(n):
            if n < 2:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        freqs = collections.defaultdict(int)
        
        m = len(mat)
        n = len(mat[0])
        directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]] #first is col
        
        def valid(nrow,ncol):
            return 0 <= nrow < m  and 0 <= ncol < n
        
        for row in range(m):
            for col in range(n):
                start = mat[row][col]
                for cp, rp in directions:
                    val = start
                    nrow = row + rp
                    ncol = col + cp
                    while valid(nrow,ncol):
                        val = 10 * val + mat[nrow][ncol]
                        freqs[val] += 1
                        nrow = nrow + rp
                        ncol = ncol + cp
                        
        keylist = list(freqs.keys())
        primes = []
        for key in keylist:
            if is_prime(key):
                primes.append(key)
                
        curr = 0
        ans = -1
        for prime in primes:
            if freqs[prime] > curr:
                ans = prime
                curr = freqs[prime]
            elif freqs[prime] == curr:
                ans = max(ans,prime)
        
        return ans
        