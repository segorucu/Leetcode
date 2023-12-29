from functools import cache
class Solution:
    def __init__(self):
        self.minval = float("inf")
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        if len(jobDifficulty) < d:
            return -1
        elif len(jobDifficulty) == d:
            return sum(jobDifficulty)
        n = len(jobDifficulty)


        @cache
        def dp(i,j,cur_max):
            if i == n:
                return 0 if j == 0 else float("inf")
            if j == 0:
                return float("inf")

            cur_max = max(cur_max,jobDifficulty[i])

            hold = dp(i+1,j,cur_max)
            move =dp(i+1,j-1,0) + cur_max
            return min(hold,move)
            
        return dp(0,d,-1)
        