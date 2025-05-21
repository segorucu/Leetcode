from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        countert = Counter(t)
        counters = Counter()

        minlen = [inf]
        ans = [""]
        def canmove(l):
            for k,v in countert.items():
                if counters[k] < v:
                    return False
            return True



        l = 0
        r = 0
        
        while r < len(s):
            counters[s[r]] += 1
            while l < len(s) and canmove(l):
                if r-l+1 < minlen[0]:
                    minlen[0] = r-l+1
                    ans[0] = s[l:r+1]
                # if s[l] in countert and counters[s[l]] == countert[s[l]]:
                #     break
                counters[s[l]] -= 1
                l += 1

                
            r += 1

        return ans[0]

            

            



        return 


        