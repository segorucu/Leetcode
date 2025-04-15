class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n = len(nums)
        minleft = n * [0]
        minval = inf
        for i,num in enumerate(nums):
            minleft[i] = minval
            minval = min(minval, num)

        maxright = n * [0]
        maxval = -inf
        for i in range(n-1,-1,-1):
            maxright[i] = maxval
            maxval = max(maxval, nums[i])

        for i in range(1,n-1):
            if minleft[i] < nums[i] < maxright[i]:
                return True
        return False

            