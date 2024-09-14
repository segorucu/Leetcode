class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:

        n = len(s)
        ans = []
        for i in range(n):
            ans.append(s[(i+k)%n])
        
        return ''.join(ans)
        