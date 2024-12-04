class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        base = ord("a")
        str1 = [ord(ch)-base for ch in str1]
        str2 = [ord(ch)-base for ch in str2]
        MOD = 26
        p2 = 0
        if len(str1) < len(str2):
            return False

        for p1 in range(len(str1)):
            n1 = str1[p1]
            if str2[p2] == n1 or str2[p2] == (n1+1)%MOD:
                p2 += 1
            if p2 == len(str2):
                return True
        return False