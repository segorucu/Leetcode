from itertools import groupby
class Solution:
    def maximumLength(self, s: str) -> int:
        
        occurences = collections.defaultdict(list)
        for k,v in groupby(s):
            l = len(list(v))
            occurences[k].append(l)

        ans = -1
        for k,v in occurences.items():
            v.sort(reverse=True)
            if sum(v) < 3:
                continue
            if len(v) >= 1:
                ans = max(ans,v[0]-2)
                if len(v) >= 2:
                    if v[1] >= v[0]-1:
                        ans = max(ans,v[0]-1)
                    if len(v) >= 3:
                        if v[0] == v[1] == v[2]:
                            ans = max(ans,v[0])


        return ans