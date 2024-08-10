class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxleft = n * [0]
        maxright =  n * [0]
        maxval = nums[0]
        for i in range(1,n-1):
            maxleft[i] = maxval
            maxval = max(maxval,nums[i])

        maxval = nums[-1]
        for i in range(n-2,0,-1):
            maxright[i] = maxval
            maxval = max(maxval,nums[i])

        ans = 0
        for i in range(1,n-1):
            curr = (maxleft[i]-nums[i]) * maxright[i]
            ans = max(ans, curr)


        return ans
