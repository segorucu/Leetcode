class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        stack = []
        for i,h in enumerate(heights):
            while stack and stack[-1][1] <= h:
                stack.pop()
            stack.append((i,h))

        ans = []
        for i,h in stack:
            ans.append(i)
        return ans