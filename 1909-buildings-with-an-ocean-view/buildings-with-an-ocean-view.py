class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        stack = []
        ans = []
        for i,h in enumerate(heights):
            while stack and stack[-1] <= h:
                stack.pop()
                ans.pop()
            stack.append(h)
            ans.append(i)

        return ans