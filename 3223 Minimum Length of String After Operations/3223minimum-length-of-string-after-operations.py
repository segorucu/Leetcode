class Solution:
    def minimumLength(self, s: str) -> int:
        

        counter = collections.Counter(s)
        ans = 0
        for key, val in counter.items():
            if val % 2 == 0:
                ans += 2
            else:
                ans += 1

        return ans