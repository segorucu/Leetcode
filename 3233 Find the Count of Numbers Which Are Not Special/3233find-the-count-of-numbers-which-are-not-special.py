class Solution:
    def SieveOfEratosthenes(self,start,num):
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
        # print(prime)
        # Print all prime numbers
        count = 0
        for p in range(max(start,2), num+1):
            if prime[p]:
                count += 1
        return count

    def nonSpecialCount(self, l: int, r: int) -> int:

        start = math.ceil(l**0.5)
        end = math.floor(r**0.5)
        count = self.SieveOfEratosthenes(start,end)
        # print(count)

        return r-l+1-count
        

