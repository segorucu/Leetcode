class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        base = ord('A')
        mp = {}
        visited = set()
        for a in word:
            visited.add(ord(a))
        
        count = 0
        for i in range(26):
            big = base + i
            sm = big + 32
            if big in visited and sm in visited:
                count += 1
            
        
                    
                
        return count