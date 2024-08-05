class Solution:
    def numWays(self, s: str) -> int:

        MOD = 10**9+7
        Nones = s.count("1")
        if Nones % 3 != 0:
            return 0
        third = Nones // 3

        n = len(s)
        if Nones == 0:
            return ((n-1)*(n-2) // 2) % MOD


        prefix = [0]
        for a in s:
            prefix.append(prefix[-1])
            if a == "1":
                prefix[-1] += 1

        ans = 1 
        one = two = three = 0
        for val in prefix:
            if val == third:
                one += 1
            elif val == third * 2:
                two += 1
            elif val == Nones:
                three += 1

        ans = (one*two) % MOD


        return ans

        
        