class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = n * [None]
        maxval = max(nums)
        stack = []
        for i,num in enumerate(nums):
            while stack and stack[-1][0] < num:
                val, ind = stack.pop()
                ans[ind] = num
            if num == maxval:
                ans[i] = -1
            else:
                stack.append((num,i))

        i = 0
        while stack:
            while stack and stack[-1][0] < nums[i]:
                val, ind = stack.pop()
                ans[ind] = nums[i]
            i += 1

        return ans
        
            