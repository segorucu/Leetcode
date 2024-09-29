class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        vowels = {"a","e","i","o","u"}
        counter = {}
        n = len(word)
        r = 0
        l = 0
        ans = consonants = 0
        while r < n:
            if word[r] in vowels:
                counter[word[r]] = r
            else:
                consonants += 1
            r += 1
            if consonants < k:
                continue

            while consonants > k:
                if word[l] in vowels:
                    if l >= counter[word[l]]:
                        del counter[word[l]]
                else:
                    consonants -= 1
                l += 1

            if len(counter) == 5:
                l2 = l
                while word[l2] in vowels:
                    if l2 >= counter[word[l2]]:
                        break
                    l2 += 1
                ans += (l2 - l + 1)
                # print(l,r,ans)

        return ans
        