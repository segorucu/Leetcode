class Solution:
    def isNumber(self, s: str) -> bool:
        validset = {
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "e", "E", "-", "+"
        }
        integerset = {
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
        }

        def checkinteger(txt):
            if len(txt) == 0:
                return False
            digit = 0
            left = 0
            if txt[left] in {"+","-"}:
                left += 1
            while left < len(txt):
                if txt[left] not in integerset:
                    return False
                left += 1
                digit += 1
            return digit > 0

        def checkdecimal(txt):
            if len(txt) == 0:
                return False
            digit = 0
            left = 0
            if txt[left] in {"+","-"}:
                left += 1
            dot = False
            while left < len(txt):
                if txt[left] in integerset:
                    digit += 1
                elif txt[left] == "." and not dot:
                    dot = True
                else:
                    return False
                left += 1
            return digit > 0

            
        if "e" in s or "E" in s:
            # right is integer
            # left is either integer or decimal
            
            for i,c in enumerate(s):
                if c in {"e","E"}:
                    ind = i
                    break
            if not checkinteger(s[ind+1:]):
                return False
            if not checkdecimal(s[0:ind]):
                return False
        elif "." in s:
            #decimal
            if not checkdecimal(s):
                return False
        else:
            #integer
            if not checkinteger(s):
                return False
                
        return True