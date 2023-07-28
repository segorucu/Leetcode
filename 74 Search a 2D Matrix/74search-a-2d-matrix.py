class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        up = 0
        low = m-1
        left = 0
        right = n-1
        row = -100
        while up <= low:
            mid = (up + low) // 2
            if matrix[mid][left] <= target <= matrix[mid][right]:
                row = mid
                break
            elif target > matrix[mid][right]:
                up = mid + 1
            else:
                low = mid - 1

        if row == -100:
            return False

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False
