from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransom = defaultdict(int)
        for c in ransomNote:
            ransom[c] += 1
        mag = defaultdict(int)
        for c in magazine:
            mag[c] += 1
            
        for key, val in ransom.items():
            if val > mag[key]:
                return False
            
        return True