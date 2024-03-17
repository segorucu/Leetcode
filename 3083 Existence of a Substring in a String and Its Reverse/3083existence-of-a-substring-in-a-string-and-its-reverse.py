class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        
        rev = s[::-1]
        
        n = len(s)
        for i in range(n-1):
            if s[i:i+2] in rev:
                # print(s[i])
                return True
        return False
        