from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = Counter(s)
        ct = Counter(t)
        
        diff = 0
        for key in cs.keys() | ct.keys():
            if cs[key] - ct[key] > 0:
                diff += cs[key] - ct[key]

        return diff
        