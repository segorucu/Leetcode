class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == 0:
            return 0

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            add = -1
        else:
            add = 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = len(range(0,dividend-divisor+1,divisor))
        minus_limit = -(2**31)
        max_limit = 2**31-1

        if add == -1:
            ans = -ans
            ans = max(minus_limit,ans)
            return ans

        ans = min(ans,max_limit)
        return ans



            