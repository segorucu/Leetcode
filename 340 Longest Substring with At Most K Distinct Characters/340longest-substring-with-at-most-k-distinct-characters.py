class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        counter = collections.defaultdict(int)

        l = 0
        n = len(s)
        ans = 0
        for r in range(n):
            counter[s[r]] += 1
            while len(counter) > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    counter.pop(s[l])
                l += 1

            ans = max(ans,(r-l+1))

        return ans