class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:


        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                top = matrix[r-1][c] if r > 0 else 0
                left = matrix[r][c-1] if c > 0 else 0
                top_left = matrix[r-1][c-1] if min(r,c) > 0 else 0
                matrix[r][c] += top + left - top_left

        res = 0
        for r1 in range(ROWS):
            for r2 in range(r1,ROWS):
                count = collections.defaultdict(int)
                count[0] = 1
                for c in range(COLS):
                    cur_sum = matrix[r2][c]
                    if r1 > 0:
                        cur_sum -= matrix[r1-1][c]
                    diff = cur_sum - target
                    if diff in count:
                        res += count[diff]
                    count[cur_sum] += 1
                  
        return res
        