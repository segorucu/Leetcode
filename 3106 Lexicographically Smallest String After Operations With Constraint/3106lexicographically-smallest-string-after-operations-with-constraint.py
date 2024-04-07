class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        
        base = ord('a')
        end = ord('z')

        result = []
        for val in s:
            # first option
            if k == 0:
                result.append(val)
                continue
                
            diff = min(ord(val)-base,end-ord(val)+1)
            if diff <= k:
                result.append("a")
                k -= diff
                continue
            else:
                curr = ord(val) - k
                result.append(chr(curr))
                k = 0
                
            

            
        return ''.join(result)

