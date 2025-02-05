class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        c1 = Counter(s1)
        c2 = Counter(s2)
        if c1 != c2:
            return False

        tot = 0
        for c1,c2 in zip(s1,s2):
            if c1 != c2:
                tot += 1
        return tot <= 2