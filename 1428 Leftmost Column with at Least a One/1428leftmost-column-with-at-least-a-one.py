# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        ans = float("inf")

        for row in range(m):
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                val = binaryMatrix.get(row,mid)
                if val == 0:
                    left = mid + 1
                else:
                    right = mid - 1
            if 0 <= left < n:
                ans = min(ans,left)

        if ans == float("inf"):
            return -1 

        return ans