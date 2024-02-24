from functools import cache
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words = sorted(words, key=len)
        
        # lengthmp = collections.defaultdict(list)
        # for word in words:
        #     lengthmp[len(word)].append(word)
        @cache
        def valid(word1,word2):
            mismatch = 0
            r = 0
            for l in range(len(word1)):
                while word1[l] != word2[r]:
                    mismatch += 1
                    r += 1
                    if mismatch > 1:
                        return False
                r += 1
            return mismatch <= 1

        n = len(words)
        @cache
        def backtrack(i):
            ans = 1
            for j in range(i+1,n):
                if len(words[i]) + 1 == len(words[j]) and valid(words[i],words[j]):
                    ans = max(ans,backtrack(j) + 1)
            return ans


        ans = 1
        for i in range(n):
            ans = max(ans,backtrack(i))


        return ans
        