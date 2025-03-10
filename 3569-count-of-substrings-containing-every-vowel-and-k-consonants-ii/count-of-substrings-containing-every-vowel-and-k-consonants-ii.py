class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        counter = {}
        n = len(word)
        r = 0
        l = 0
        ans = 0
        consonants = collections.deque()
        while r < n:
            if word[r] in vowels:
                counter[word[r]] = r
            else:
                consonants.append(r)
            r += 1
            if len(consonants) < k:
                continue

            while len(consonants) > k:
                if word[l] in vowels:
                    if l >= counter[word[l]]:
                        del counter[word[l]]
                else:
                    consonants.popleft()
                l += 1

            if len(counter) == 5:
                l2 = min(counter.values())
                if consonants:
                    l2 = min(l2, consonants[0])
                ans += (l2 - l + 1)

        return ans
        