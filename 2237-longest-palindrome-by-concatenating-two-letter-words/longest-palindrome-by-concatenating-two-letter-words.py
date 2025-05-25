class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        counter = Counter(words)

        keys = counter.keys()
        tot = 0
        odd = 0
        for key in counter:
            rev = key[:][::-1]
            if key == rev:
                if counter[key] % 2:
                    odd = 2
                tot += 4 * (counter[key] // 2)
            else:
                if rev in counter:
                    occ = min(counter[key],counter[rev])
                    tot += occ * 4
                    counter[key] -= occ
                    counter[rev] -= occ

        return tot + odd

