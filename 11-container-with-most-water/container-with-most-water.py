class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        ans = 0
        while left < right:
            dum = (right-left) * min(height[left],height[right])
            if dum > ans:
                ans = dum
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return ans

    