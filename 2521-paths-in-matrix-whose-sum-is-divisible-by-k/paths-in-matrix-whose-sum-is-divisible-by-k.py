class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        
        # (2,2): 2: 1

        # (2,1): 0: 1

        # (2,0): 0: 1

        # (1,2): 1: 1

        # (1,1): 0: 1  1: 1
        # (1,0): 0: 2  1: 1

        # (0,2): 2: 1
        # (0,1): 0: 1 1: 1  2: 1
        # (0,0): 0: 2 1: 1  2: 3

        M = len(grid)
        N = len(grid[0])
        MOD = 10**9+7

        dp = collections.defaultdict(lambda: defaultdict(int))
        def valid(r,c):
            return 0 <= r < M and 0 <= c < N

        dp[(M-1,N-1)][grid[M-1][N-1]%k] = 1
        for c in range(N-1, -1, -1):
            for r in range(M-1, -1, -1):
                neighs = [(r+1,c),(r,c+1)]
                curr = grid[r][c]
                for nr, nc in neighs:
                    if not valid(nr,nc):
                        continue
                    for key, val in dp[(nr, nc)].items():
                        dp[(r,c)][(key + curr) % k] += val
                        dp[(r,c)][(key + curr) % k] = dp[(r,c)][(key + curr) % k] % MOD


        return dp[(0,0)][0]



      