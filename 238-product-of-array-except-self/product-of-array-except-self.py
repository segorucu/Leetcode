class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        prefix = []
        curr = 1
        for i in range(n):
            curr *= nums[i]
            prefix.append(curr)

        suffix = n * [0]
        curr = 1
        for i in range(n-1,-1,-1):
            curr *= nums[i]
            suffix[i] = curr

        ans = n * [0]
        for i in range(n):
            curr = 1
            if i > 0:
                curr *= prefix[i-1]
            if i < n-1:
                curr *= suffix[i+1]

            ans[i] = curr

        return ans