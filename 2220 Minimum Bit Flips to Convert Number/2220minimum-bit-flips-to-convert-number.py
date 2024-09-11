class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        flip = 0
        while start or goal:
            if start % 2 != goal % 2:
                flip += 1
            start = start >> 1
            goal = goal >> 1
        return flip
