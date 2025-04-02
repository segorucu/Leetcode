class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        lefttorightmax = []
        maxval = -inf
        for num in nums:
            lefttorightmax.append(maxval)
            maxval = max(maxval, num)

        n = len(nums)
        righttoleftmax = n * [0]
        maxval = -inf
        for i in range(n-1,-1,-1):
            righttoleftmax[i] = maxval
            maxval = max(maxval, nums[i])

        # print(righttoleftmax)

        ans = 0
        for i in range(1,n-1):
            curr = (lefttorightmax[i] - nums[i]) * righttoleftmax[i]
            ans = max(ans, curr)
        # print(ans)
        return ans
            
            
