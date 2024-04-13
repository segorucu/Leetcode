class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
            
        maxArea = 0
        stack = []
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea,height * (i-index))
                start = index
            stack.append((start,h))
        
        for i,h in stack:
            maxArea = max(maxArea,h * (len(heights) - i))

        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1,m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = matrix[i-1][j] + 1

        res = 0
        for i in range(m):
            res = max(res,self.largestRectangleArea(matrix[i]))

        return res
        