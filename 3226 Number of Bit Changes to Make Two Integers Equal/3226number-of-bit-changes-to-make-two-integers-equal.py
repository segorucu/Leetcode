class Solution:
    def minChanges(self, n: int, k: int) -> int:
        
        count = 0
        while n > 0 or k > 0:
            if (n % 2 == 1) and (k % 2 == 0):
                count += 1
            elif (n % 2 == 0) and (k % 2 == 1):
                return -1
            n = n >> 1
            k = k >> 1

        return count

        