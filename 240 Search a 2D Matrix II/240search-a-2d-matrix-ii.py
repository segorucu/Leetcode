class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if target < matrix[0][0]:
            return False
        elif target == matrix[0][0]:
            return True
        elif target > matrix[-1][-1]:
            return False

        # top = 0
        # bottom = m - 1
        # while top <= bottom:
        #     mid = (top + bottom) // 2
        #     if matrix[mid][0] > target:
        #         top = mid + 1
        #     else:
        #         bottom = mid - 1

        for i in range(m):
            if matrix[i][0] > target:
                return False
            left = 0
            right = n-1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
