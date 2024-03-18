class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        
        nums.sort()
        n = len(nums)
        ans = n * [0]
        l = 0
        r = n-1
        for i in range(n):
            if i % 2 == 0:
                ans[i] = nums[l]
                l += 1
            else:
                ans[i] = nums[r]
                r -= 1
        return ans


        return nums