class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        stack = []
        maxval = -inf
        beg = inf
        end = 0
        for i, num in enumerate(nums):
            while stack and stack[-1][1] > num:
                _, _, ind = stack.pop()
                beg = min(beg, ind)
                end = max(end, i)

            maxval = max(maxval,num)
            stack.append((num,maxval,i))

        if beg == inf:
            return 0
        return end - beg + 1