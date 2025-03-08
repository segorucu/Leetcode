class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        if k > len(s):
            return 0
            
        counter = collections.defaultdict(int)
        for i in range(k):
            counter[s[i]] += 1

        ans = 0
        if len(counter) == k:
            ans += 1

        for i in range(k,len(s)):
            counter[s[i]] += 1
            l = i-k
            counter[s[l]] -= 1
            if counter[s[l]] == 0:
                del counter[s[l]]
            if len(counter) == k:
                ans += 1

        return ans


        