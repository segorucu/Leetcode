class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        if (sx,sy) == (fx,fy):
            return t != 1
        dist = max(abs(sx-fx),abs(sy-fy))
        if dist <= t:
            return True

        return False

            
        