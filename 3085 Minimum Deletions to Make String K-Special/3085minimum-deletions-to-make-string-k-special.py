class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        counter = collections.Counter(word)
        vals = sorted(counter.values())
        ans = float("inf")
        for val in vals:
            sm = 0
            maxaccepted = val + k
            minaccepted = val
            for i in range(len(vals)):
                val2 = vals[i]
                if val2 > maxaccepted:
                    sm += (val2 - maxaccepted)
                elif val2 < minaccepted:
                    sm += val2
            if sm < ans:
                ans = sm
        return ans
            