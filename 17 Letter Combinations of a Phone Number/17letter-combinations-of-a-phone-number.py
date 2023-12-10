class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {'2':['a','b','c'],
              '3':['d','e','f'],
              '4':['g','h','i'],
              '5':['j','k','l'],
              '6':['m','n','o'],
              '7':['p','q','r','s'],
              '8':['t','u','v'],
              '9':['w','x','y','z']}
        
        final = []
        def Backtrack(i,curr):
            if len(curr) == len(digits):
                final.append(curr)
                return

            for c in mp[digits[i]]:
                curr += c
                Backtrack(i+1,curr)
                curr = curr[:-1]

        if digits:
            Backtrack(0,"")
        return final
    
            
                    
                
        
            
        