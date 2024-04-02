class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mp = collections.defaultdict(str)

        values = set()
        for a,b in zip(s,t):
            if a in mp:
                if mp[a] != b:
                    return False
            else:
                if b in values:
                    return False
                mp[a] = b
                values.add(b)
            # print(mp)

        return True

        
        