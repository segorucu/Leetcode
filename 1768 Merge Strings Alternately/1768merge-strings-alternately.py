class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ans = []
        for a, b in zip(word1,word2):
            ans.append(a)
            ans.append(b)
        len1 = len(word1)
        len2 = len(word2)
        if len1 == len2:
            pass
        elif len1 > len2:
            ans.append(word1[len2:])
        else:
            ans.append(word2[len1:])

        ans = "".join(ans)
        
        
        return ans