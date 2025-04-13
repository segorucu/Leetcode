class Solution:
    def judgeSquareSum(self, c: int) -> bool:


        for a in range(int(c**0.5)+1):
            a2 = a ** 2
            b2 = c - a2
            if (int(b2**0.5))**2 == c- a2:
                return True

        return False