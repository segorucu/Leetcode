class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        
        curr = x
        n -= 1
        i = 0
        while n:
            n, rem = divmod(n,2)
            mask = 1 << i
            while mask & x == mask:
                i += 1
                mask = 1 << i
            x = x | (rem << i)
            i += 1
            
        return x