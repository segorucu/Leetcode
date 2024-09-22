class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        
        c2 = collections.Counter(word2)
        c1 = collections.Counter()

        l = 0
        n = len(word1)
        r = 0
        ans = 0
        completed = False
        while r < n:
            a = word1[r]
            c1[a] += 1
            for key, val in c2.items():
                if c1[key] < val:
                    break
            else:
                completed = True
            if not completed:
                r += 1
                continue
            left = word1[l]
            while c1[left] > c2[left]:
                l += 1
                c1[left] -= 1
                left = word1[l]
            r += 1
            ans += l+1

        return ans

