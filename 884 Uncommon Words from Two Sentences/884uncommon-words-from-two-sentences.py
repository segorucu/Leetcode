class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        first = collections.Counter(s1.split())
        second = collections.Counter(s2.split())
        ans = set()
        for a in s2.split():
            if a not in first and second[a] == 1:
                ans.add(a)
        for a in s1.split():
            if a not in second and first[a] == 1:
                ans.add(a)

        return list(ans)