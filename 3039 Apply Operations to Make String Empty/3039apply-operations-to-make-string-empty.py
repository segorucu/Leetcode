class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        
        counter = collections.Counter(s)
        ops = max(counter.values())-1
        freqs = collections.defaultdict(int)
        
        arr = []
        for a in s:
            if freqs[a] >= ops:
                arr.append(a)
            freqs[a] += 1
            
        ans = "".join(arr)
        return ans