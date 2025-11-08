class Solution:
    def smallestNumber(self, n: int) -> int:
        
        add = 1
        curr = 0
        filled = False

        while n:
            if not (curr & 1):
                filled = True
            curr += add
            add = add << 1
            n = n >> 1

        if not filled:
            curr += add

        return curr