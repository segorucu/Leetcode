from functools import cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        
        mp = collections.defaultdict(list)
        for sub in dictionary:
            size = len(sub)
            beg = -1
            while True:
                beg = s.find(sub,beg+1)
                if beg < 0:
                    break
                mp[beg].append(size)

        n = len(s)
        @cache
        def backtrack(i,tot):
            # print(i,tot)
            if i >= n:
                return tot

            res = backtrack(i+1,tot)
            for neigh in mp[i]:
                # print("h", i, neigh)
                res = min(res,backtrack(i+neigh,tot-neigh))
            return res

        return backtrack(0,n)
