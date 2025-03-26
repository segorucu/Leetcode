class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        n = len(heights)

        maxh = 0
        arr = []
        for i in range(n-1,-1,-1):
            if heights[i] > maxh:
                arr.append(i)
                maxh = max(maxh, heights[i])

        return list(reversed(arr))