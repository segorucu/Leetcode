class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        

        mp = {}
        
        for i,a in enumerate(word):
            if ord(a) >= ord('a'):
                mp[ord(a)] = i
            else:
                if ord(a) not in mp:
                    mp[ord(a)] = i
                    
        # print(mp)
        
        count = 0
            
        base = ord('A')
        for i in range(26):
            big = base + i
            sm = big + 32
            if big in mp and sm in mp and mp[big] > mp[sm]:
                count += 1
        
         
        return count