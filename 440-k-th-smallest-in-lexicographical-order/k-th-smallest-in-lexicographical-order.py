class Solution:
    def numbercount(self, n, prefix1, prefix2):
        steps = 0
        while prefix1 <= n:
            steps += min(prefix2,n+1) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        
        curr = 1
        k -= 1

        while k > 0:
            steps = self.numbercount(n, curr, curr+1)

            if steps <= k:
                k -= steps
                curr += 1
            else:
                k -= 1
                curr *= 10

        return curr

1        
