class Solution:
    def myAtoi(self, s: str) -> int:
        listofints = ['0','1','2','3','4','5','6','7','8','9']
        signs = ['-','+']
        val = ''
        sign = '+'
        signread = False
        for c in s:
            if c == ' ':
                if not signread and val == '':
                    continue
                else:
                    break
            if c in signs and not signread:
                signread = True
                if val == '':
                    sign = c
                    continue
                else:
                    break
            if c in listofints:
                val += c
                continue 
            break
        
        if val == '': return 0
        dum = int(val)
        if sign == '-': dum *= -1
        dum = min(2**31-1,dum)
        dum = max(-2**31,dum)
        return dum
            
