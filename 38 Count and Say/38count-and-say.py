class Solution:
    def countAndSay(self, n: int) -> str:

        def recurse(i):
            if i == 1:
                return "1"

            orig = recurse(i-1)
            m = len(orig)
            prev = orig[0]
            ans = ""
            count = 1
            for j in range(1,m):
                if orig[j] != prev:
                    ans += str(count) + prev
                    prev = orig[j]
                    count = 1
                else:
                    count += 1
            ans += str(count) + prev
            return ans

        return recurse(n)







        return ans

        