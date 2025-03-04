class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        maxval = min(10**7,n)
        arr = []
        curr = 1
        while curr <= maxval:
            arr.append(curr)
            curr *= 3


        while n > 0 and arr:
            curr = arr.pop()
            # print(n,curr)
            if curr <= n:
                n -= curr
            


        return n == 0
        