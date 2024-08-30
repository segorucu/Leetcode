class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        
        n = len(heights)
        while volume > 0:
            l = k - 1
            while l >= 0 and heights[l] <= heights[l+1]:
                l -= 1
            l = max(l,0)
            while l < k and heights[l] >= heights[l+1]:
                l += 1
            if l < k:
                heights[l] += 1
                volume -= 1
                continue
            r = k + 1
            while r < n and heights[r] <= heights[r-1]:
                r += 1
            r = min(r,n-1)
            while r > k and heights[r] >= heights[r-1]:
                r -= 1
            heights[r] += 1
            volume -=1

        return heights
            
