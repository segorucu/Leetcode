class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        n = len(s)
        ans = 0
        l = 0
        counter = collections.defaultdict(int)
        for r in range(n):
            counter[s[r]] += 1
            if len(counter) < 3:
                continue
            while counter[s[l]] > 1:
                counter[s[l]] -= 1
                l += 1
            ans += l + 1

        return ans
