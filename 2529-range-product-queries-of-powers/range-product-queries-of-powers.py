from bisect import bisect
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        powers = []
        if n % 2 == 1:
            powers.append(1)
            n -= 1

        MOD = 10**9+7

        options = []
        for p in range(1,31):
            options.append(2**p)

        while n:
            ind = bisect(options,n)
            if options[ind] == n:
                powers.append(n)
                n = 0
            else:
                powers.append(options[ind-1])
                n -= options[ind-1]

        powers.sort()
        
        ans = []
        for l,r in queries:
            curr = 1
            for i in range(l,r+1):
                curr *= powers[i]
                curr = curr % MOD
            ans.append(curr)
        return ans




        return []