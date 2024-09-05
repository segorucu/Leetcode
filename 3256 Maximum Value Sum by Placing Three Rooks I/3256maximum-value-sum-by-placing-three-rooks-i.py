from functools import cache
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        
        m = len(board)
        n = len(board[0])
        
        arr = collections.defaultdict(list)
        for r in range(m):
            tmp = []
            for c in range(n):
                tmp.append((board[r][c],c))
            tmp.sort(reverse=True)
            arr[r].extend(tmp[0:3])

        @cache
        def dp(row, count, c1, c2):
            if count == 3:
                return 0

            if row == m:
                return -inf

            best = dp(row+1, count, c1, c2)
            for x, index in arr[row]:
                if index in {c1,c2}:
                    continue
                if c1 == -1:
                    best = max(best, dp(row+1, count+1, index, c2) + x)
                elif c2 == -1:
                    best = max(best, dp(row+1, count+1, c1, index) + x)
                else:
                    best = max(best, dp(row+1, count+1, c1, c2) + x)
            return best
        
        return dp(0,0,-1,-1)
            
        
        