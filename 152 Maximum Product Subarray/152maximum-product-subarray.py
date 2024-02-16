class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)

        def findmax(l,r):
            if l >= r:
                return -10
            prod = prefix[r] // prefix[l]
            if  prod > 0:
                return prod
            else:
                return max(findmax(l+1,r),findmax(l,r-1))

        l = 0
        r = 0
        ans = max(nums)
        while r < n:
            prefix = [1]
            while r < n and nums[r] != 0:
                prefix.append(prefix[-1]*nums[r])
                r += 1
            ans = max(ans,findmax(0,len(prefix)-1))
            while r < n and nums[r] == 0:
                r += 1
                l = r
        
        return ans
                
