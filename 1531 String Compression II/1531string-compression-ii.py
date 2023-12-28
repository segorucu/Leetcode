from functools import cache
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        @cache
        def dp(i,k,prev,prev_count):
            if k < 0:
                return float("inf")
            if i == len(s):
                return 0

            if s[i] == prev:
                incr = 1 if prev_count in {1,9,99} else 0
                res = incr + dp(i+1,k,s[i],prev_count+1)
            else:
                 delete = dp(i+1,k-1,prev,prev_count)
                 keep = 1 + dp(i+1,k,s[i],1)
                 res = min(keep,delete)
                
            return res
       




        return dp(0,k,"",0)