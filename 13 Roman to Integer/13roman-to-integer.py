class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        sum = 0
        while(i<len(s)):
            c = s[i]
            try:
                p = s[i+1]
                if c=="I" and p =="V":
                    sum += 4
                    i += 2
                    continue
                elif c=="I" and p =="X":
                    sum += 9
                    i += 2
                    continue
                elif c=="X" and p =="L":
                    sum += 40
                    i += 2
                    continue
                elif c=="X" and p =="C":
                    sum += 90
                    i += 2
                    continue
                elif c=="C" and p =="D":
                    sum += 400
                    i += 2
                    continue
                elif c=="C" and p =="M":
                    sum += 900 
                    i += 2
                    continue
            except:
                pass
            if c == "I":
                sum += 1
            elif c == "V":
                sum += 5
            elif c == "X":
                sum += 10
            elif c == "L":
                sum += 50
            elif c == "C":
                sum += 100
            elif c == "D":
                sum += 500
            elif c == "M":
                sum += 1000
            i += 1
        return sum
                    
                    
            