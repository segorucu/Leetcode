class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @cache
        def dp(Alice,n): 
            if n == 0:
                if Alice:
                    return False
                else:
                    return True
            
            largestsq = int(math.pow(n,0.5))

            if Alice:
                for i in range(1, largestsq+1):
                    take = i**2
                    if dp(False,n-take):
                        return True
                return False
            else:
                win = True
                for i in range(1, largestsq+1):
                    take = i**2
                    if not dp(True,n-take):
                        return False
                return True

        return dp(True,n)

        # dp(True,7)
        # n = 7
        # largestsq = 2
        # i = 1
        # take = 1
        # maxval = 0

        # dp(False,6)
        # n = 6
        # largestsq = 2
        # i = 1
        # take = 1
        # minval = inf

        # dp(True,5)
        # n = 5
        # largestsq = 2
        # i = 1
        # take = 1
        # maxval = 0

        # dp(False,4)
        # n = 4
        # largestsq = 2
        # i = 2
        # take = 4
        # minval = inf

        # dp(True,3)
        # n = 3
        # largestsq = 1
        # i = 1
        # take = 1
        # maxval = inf
        # return inf

        # dp(False, 2)
        # n = 2
        # largestsq = 1
        # i = 1
        # take = 1
        # minval = inf
        # return inf

        # dp(True,1)
        # n = 1
        # return inf

        