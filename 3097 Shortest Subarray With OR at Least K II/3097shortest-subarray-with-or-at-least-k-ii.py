class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        maxval = max(nums)
        if maxval >= k:
            return 1

        maxind = 0
        curr = maxval
        while curr:
            curr = curr >> 1
            maxind += 1

        curr = k
        kind = 0
        while curr:
            curr = curr >> 1
            kind += 1

        if kind > maxind:
            return -1

        bitcount = 31 * [0]
        l = 0
        OR = 0
        ans = inf
        for i, num in enumerate(nums):
            OR = OR | num
            for bit in range(31):
                if num & (1 << bit):
                    bitcount[bit] += 1

            while OR >= k and l < i:
                ans = min(ans, i-l+1)
                tmpOR = 0
                for bit in range(31): 
                    if nums[l] & (1 << bit):
                        bitcount[bit] -= 1
                    if bitcount[bit] > 0:
                        tmpOR |= (1<<bit)
                OR = tmpOR
                l += 1

        if ans == inf:
            return -1
        return ans 

