class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        alphabet = set(s)
        dates = defaultdict(list)
        for i,a in enumerate(s):
            dates[a].append(i)

        stack = []
        for k,v in dates.items():
            stack.append([v[0],v[-1]])

        stack.sort()

        maxdate = -1
        ans = []
        beg = 0
        for b,e in stack:
            if b > maxdate:
                if maxdate > -1:
                    ans.append(maxdate-beg+1)
                beg = b
            maxdate = max(maxdate, e)
        ans.append(maxdate-beg+1)

        return ans
        