class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        MOD = 10**9 + 7
        multiples = set()
        n = 1
        while n <= 2*max(deliciousness):
            multiples.add(n)
            n *= 2

        counter = collections.defaultdict(int)

        ans = 0
        for one in deliciousness:
            for tot in multiples:
                two = tot - one
                ans += counter[two]
                ans %= MOD
            counter[one] += 1

        return ans 