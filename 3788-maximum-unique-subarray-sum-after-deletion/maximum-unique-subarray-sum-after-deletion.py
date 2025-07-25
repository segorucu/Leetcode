class Solution:
    def maxSum(self, nums: List[int]) -> int:
        

        
        stack = []
        for num in nums:
            if num > 0:
                stack.append(num)
        if not stack:
            return max(nums)

        n = len(stack)  
        counter = defaultdict(int)
        sm = 0
        for num in stack:
            if num not in counter:
                sm += num
            counter[num] += 1

        return sm

