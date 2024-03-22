class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        stack = []
        maxval = 0
        for i, num in enumerate(arr):
            changed = False
            while stack and stack[-1][1] > num:
                stack.pop()
            maxval = max(maxval, num)
            stack.append((num,maxval))
        
        return len(stack)
        