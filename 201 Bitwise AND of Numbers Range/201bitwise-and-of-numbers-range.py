class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        if min(left,right) == 0:
            return 0
        if left == right:
            return left
        dum = right
        digitsr = 0
        while dum > 0:
            dum = dum // 2
            digitsr += 1
        dum = left
        digitsl = 0
        while dum > 0:
            dum = dum // 2
            digitsl += 1
        if right - left > 32:
            if digitsl == digitsr: 
                return 2**(digitsl-1)
            else:
                return 0

        ans = left
        i = left + 1
        while i < right + 1:
            ans = ans & i
            i += 1
        return ans
        