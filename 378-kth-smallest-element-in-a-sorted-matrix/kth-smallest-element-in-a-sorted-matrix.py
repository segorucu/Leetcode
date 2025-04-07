class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[-1][-1]

        def count(mid):
            cnt = 0
            for row in range(n):
                col = bisect_right(matrix[row],mid)
                if col == n:
                    cnt += n
                elif matrix[row][col] == mid:
                    cnt += col + 1
                else:
                    cnt += col
            return cnt >= k

        res = 0
        while left <= right:
            mid = (left+right) // 2
            if count(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res



        return matrix[row][col]