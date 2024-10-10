class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        stack = []
        ans = 0
        for i, num in enumerate(nums):
            j = len(stack)-1
            while j >= 0 and stack[j][0] <= num:
                val, ind = stack[j]
                # print(i,ind)
                ans = max(ans,i-ind)
                j -= 1
            if not stack:
                stack.append((num,i))
            elif stack and num < stack[-1][0]:
                stack.append((num,i))
        return ans