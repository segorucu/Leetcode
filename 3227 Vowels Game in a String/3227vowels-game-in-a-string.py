class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        vowels = {"a","e","i","o","u"}
        tmp = set(s)
        for a in vowels:
            if a in tmp:
                return True
        return False