from sortedcontainers import SortedList
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        maxval = max(nums)

        def SieveOfEratosthenes(num):
            prime = [True for i in range(num+1)]
        # boolean array
            p = 2
            while (p * p <= num):
        
                # If prime[p] is not
                # changed, then it is a prime
                if (prime[p] == True):
        
                    # Updating all multiples of p
                    for i in range(p * p, num+1, p):
                        prime[i] = False
                p += 1
            return prime

        prime = SieveOfEratosthenes(maxval)
        primes = SortedList()
        for i in range(2,maxval+1):
            if prime[i]:
                primes.add(i)

        prev = -1
        for i in range(len(nums)):
            num = nums[i]
            for j in range(len(primes)-1,-1,-1):
                if primes[j] >= num:
                    continue
                if num - primes[j] > prev:
                    nums[i] -= primes[j]
                    break
            if i > 0 and nums[i] <= nums[i-1]:
                return False
            prev = nums[i]
            
            
        return True




        return 0

        