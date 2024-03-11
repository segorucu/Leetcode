class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        freq = collections.defaultdict(int)
        for a in s:
            freq[a] += 1

        # print(freq)
        ans = ""
        for a in order:
            ans += freq[a] * a

        for a in s:
            if a not in order:
                ans += a



        return ans