class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        c1 = collections.Counter(s1)
        r = 0
        n2 = len(s2)
        n1 = len(s1)
        c2 = collections.Counter()
        l = 0
        while r < n2:
            c2[s2[r]] += 1
            while r-l+1  > n1:
                c2[s2[l]] -= 1
                l +=1
            if r-l+1 == n1:
                if c1 == c2:
                    return True
            r += 1
        return False
