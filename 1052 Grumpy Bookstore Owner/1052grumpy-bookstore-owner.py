class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:


        l = r = 0
        n = len(customers)
        curr = 0
        maxl = -1
        maxval = 0
        while r < n:
            if grumpy[r]:
                curr += customers[r]
            while r-l >= minutes:
                if grumpy[l]:
                    curr -= customers[l]
                l += 1
            if curr > maxval:
                maxval = curr
                maxl = l
            r += 1

        for l in range(minutes):
            grumpy[maxl+l] = 0

        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]

        return ans
        