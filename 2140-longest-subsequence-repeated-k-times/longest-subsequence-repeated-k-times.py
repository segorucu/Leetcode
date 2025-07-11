class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        counter = Counter(s)
        candidates = set()
        arr = []
        for a in s:
            if counter[a] >= k:
                candidates.add(a)
                arr.append(a)

        s = "".join(arr)
        if len(s) == 0:
            return ""

        def is_subsequence(target):
            j = 0
            for a in s:
                if a == target[j]: j += 1
                if j == len(target): return True
            return False

        def backtrack(nxt):
            if len(nxt) > len(self.res):
                self.res = nxt
            elif len(nxt) == len(self.res):
                self.res = max(self.res, nxt)

            nxto = nxt
            for cand in candidates:
                nxt = nxto + cand
                if is_subsequence(nxt * k):
                    backtrack(nxt) 

        self.res = ""
        backtrack("")
        
        return self.res