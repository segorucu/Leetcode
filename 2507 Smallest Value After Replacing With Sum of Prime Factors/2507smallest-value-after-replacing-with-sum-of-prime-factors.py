class Solution:
    def smallestValue(self, n: int) -> int:
        
        def recursive(n):

            prev = n
            ans = 0

            for i in range(2,n+1):
                while n % i == 0:
                    ans += i
                    n = n // i
            if prev == ans:
                return ans
            else:
                return recursive(ans)

        return recursive(n)