class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        longest = 0
        for word in wordDict:
            longest = max(longest,len(word))

        n = len(s)
        ans = []
        def dp(right,curr):
            if right == 0:
                tmp = curr.copy()
                tmp.reverse()
                tmp = " ".join(tmp)
                ans.append(tmp)

            for j in range(right-1,-1,-1):
                if right - j > longest:
                    return
                if s[j:right] in wordDict:
                    curr.append(s[j:right])
                    dp(j,curr)
                    curr.pop()

        dp(n,[])
        return ans