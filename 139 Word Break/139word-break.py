class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        n = len(s)
        valid = [0]
        for i in range(n):
            m = len(valid)
            for j in range(m-1,-1,-1):
                start  = valid[j]
                if s[start:i+1] in wordDict:
                    valid.append(i+1)
                    break

        return valid[-1] == n
