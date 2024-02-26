import collections
class Solution:
    def canTraverseAllPairs(self, nums):

        N = len(nums)
        parents = [i for i in range(N)]

        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]

        def uunion(x,y):
            ua = ufind(x)
            ub = ufind(y)
            parents[ua] = ub

        MX = max(nums)

        primes = [i for i in range(MX+1)]
        for i in range(2,MX+1):
            if primes[i] == i:
                j = i*i
                while j <= MX:
                    primes[j] = i
                    j += i

        lookup = collections.defaultdict(set)
        for index, x in enumerate(nums):
            while primes[x] != x:
                lookup[primes[x]].add(index)
                x //= primes[x]
            if x > 1:
                lookup[primes[x]].add(index)

        for k in lookup.keys():
            L = list(lookup[k])
            for i in range(1,len(L)):
                uunion(L[0],L[i])

        for i in range(N):
            if ufind(i) != ufind(0):
                return False

        return True
