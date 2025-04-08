class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        count = n * [0]
        stack = []
        for i,h in enumerate(heights):
            while stack and stack[-1][0] <= h:
                _, ind = stack.pop()
                count[ind] += 1
            if stack:
                count[stack[-1][1]] += 1
            stack.append((h,i))

        return count
