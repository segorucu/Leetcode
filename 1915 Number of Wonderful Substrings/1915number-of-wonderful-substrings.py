class Solution:
    def wonderfulSubstrings(self, word: str) -> int:


        ans = 0
        counter = collections.defaultdict(int)
        counter[0] = 1
        mask = 0

        for c in word:
            ind = ord(c) - ord('a')
            mask = mask ^ (1 << ind)
            ans += counter[mask]

            for i in range(10):
                oddmask = mask ^ (1 << i)
                ans += counter[oddmask]

            counter[mask] += 1

        return ans