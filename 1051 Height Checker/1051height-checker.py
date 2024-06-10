class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        arr = heights.copy()
        arr.sort()
        tot = 0
        for a,b in zip(heights,arr):
            if a != b:
                tot += 1


        return tot