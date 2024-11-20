class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        letters = ["a","b","c"]
        counter = collections.defaultdict(int)
        n = len(s)
        for i in range(n):
            letter = s[i]
            counter[letter] += 1
            for letter in letters:
                if counter[letter] < k:
                    break
            else:
                break
        else:
            return -1

        mintime = i + 1
        l = i
        r = n-1
        while l >= 0:
            counter[s[l]] -= 1
            while counter[s[l]] < k:
                counter[s[r]] += 1
                r -= 1
            mintime = min(mintime, n-r+l-1)
            l -= 1

        return mintime 