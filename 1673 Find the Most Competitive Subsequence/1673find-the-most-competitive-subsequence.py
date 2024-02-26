class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:


        n = len(nums)

        stack = []
        len_stack = 0
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and n-i-1 >= k-len_stack:
                stack.pop()
                len_stack -= 1

            if len_stack < k:
                stack.append(num)
                len_stack += 1
            


        return stack


        