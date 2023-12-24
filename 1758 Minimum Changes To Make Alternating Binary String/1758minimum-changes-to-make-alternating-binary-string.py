class Solution:
    def minOperations(self, s: str) -> int:

        ops = 0
        ops2 = 0
        for i,c in enumerate(s):
            if i % 2 == 0:
                if c == "0":
                    ops += 1
                else:
                    ops2 += 1
            elif i % 2 == 1:
                if  c == "1":
                    ops += 1 
                else:
                    ops2 += 1
        return min(ops,ops2)       