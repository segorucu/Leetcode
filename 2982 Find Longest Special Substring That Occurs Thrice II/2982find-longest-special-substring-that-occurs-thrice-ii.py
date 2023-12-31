from collections import defaultdict, Counter
class Solution:
    def maximumLength(self, s: str) -> int:
       
        N = len(s)
        lookup = defaultdict(list)
        for v, g in groupby(s):
            lookup[v].append(len(list(g)))

        maxlen = -1
        for v, g in lookup.items():
            g.sort(reverse=True)
            if sum(g) < 3:
                continue
            if len(g) >= 1:
                maxlen = max(maxlen,g[0]-2)
            if len(g) >= 2:
                maxlen = max(maxlen,min(g[1],g[0]-1))
            if len(g) >= 3:
                maxlen= max(maxlen,g[0]-2,g[1]-1,g[2])

        return maxlen
                
        