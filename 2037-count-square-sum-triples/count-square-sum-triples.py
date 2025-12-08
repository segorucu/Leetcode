class Solution:
    def countTriples(self, n: int) -> int:
        

        c2 = set()
        for i in range(1,n+1):
            c2.add(i**2)

        ans = 0
        for a in range(1,n+1):
            for b in range(1,n+1):
                if (a**2 + b**2) in c2:
                    ans += 1

        return ans