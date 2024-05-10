class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        n = len(sequence)
        m = len(word)
        ans = 0
        for i in range(n-m+1):
            start = i
            count = 0
            while sequence[start:start+m] == word[:]:
                count += 1
                start += m
            ans = max(ans,count)

        return ans
