class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:


        maxval = right
        isPrime = (right+1) * [True]
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2,right):
            if isPrime[i]:
                j = 2*i
                while j <= maxval:
                    isPrime[j] = False
                    j += i

        prev = None
        ans = [-1,-1]
        minval = inf
        for i in range(left,right+1):
            if isPrime[i]:
                if prev and i-prev < minval:
                    minval = i-prev
                    ans =[prev,i]
                prev = i

        return ans

        return ans
        