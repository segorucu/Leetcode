class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:

        N = len(str(num))
        for x in range(num+1):
            t1 = str(x)
            y = t1[::-1]
            y = int(y)
            if x+y == num:
                return True


        return False        