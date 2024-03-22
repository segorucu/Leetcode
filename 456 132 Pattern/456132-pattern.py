class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        currmin = nums[0]
        stack = []
        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            stack.append((num,currmin))
            currmin = min(currmin,num)
        
        return False
        