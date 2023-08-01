class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            dum = mid*mid
            if dum == x:
                return mid
            elif dum < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
