class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = n * [0]
        stack = [(inf,-1)]
        for i,num in enumerate(nums):
            while num > stack[-1][0]:
                stack.pop()
            ans[i] = i-stack[-1][1]
            stack.append((num,i))

        stack = [(inf,n)]
        for i in range(n-1,-1,-1):
            num = nums[i]
            while num > stack[-1][0]:
                stack.pop()
            ans[i] += stack[-1][1]-i-1
            stack.append((num,i))

        return ans
