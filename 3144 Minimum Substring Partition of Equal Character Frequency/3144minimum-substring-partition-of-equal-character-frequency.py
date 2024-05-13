from functools import cache
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:

        
        @cache
        def validseparation(curr):
            counter = collections.Counter(curr)
            seen = set(counter.values())
            return len(seen) == 1

        @cache
        def dp(i,j):
            if j == len(s)-1:
                if not validseparation(s[i:j+1]):
                    return inf    
                return 1

            counts = dp(i,j+1)
            # print("c",counts,i,j)
            if validseparation(s[i:j+1]):
                counts = min(counts, dp(j+1, j+1) + 1)
                # print("vc",counts)
            
            return counts
            
        return dp(0,0)