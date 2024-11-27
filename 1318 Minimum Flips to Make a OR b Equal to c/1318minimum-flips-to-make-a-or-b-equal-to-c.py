class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        ops = 0
        while c:
            cbit = c % 2
            abit = a % 2
            bbit = b % 2
            if cbit == 0:
                ops += abit + bbit
            else:
                res = abit | bbit
                res = int(res)
                ops += (1-res)
            a = a >> 1
            b = b >> 1
            c = c >> 1

        while a or b:
            abit = a % 2
            bbit = b % 2
            ops += abit + bbit
            a = a >> 1
            b = b >> 1

        return ops