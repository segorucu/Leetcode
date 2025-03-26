class Solution:
    def isNumber(self, s: str) -> bool:
        validset = {
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "e", "E", "-", "+"
        }
        integerset = {
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
        }

        countexp = 0
        countsign = 0
        countdot = 0
        expi = -1
        n = len(s)
        for i,a in enumerate(s):
            if a not in validset:
                return False
            if a in {"e","E"}:
                countexp += 1
                expi = i
            if a in {"+","-"}:
                countsign += 1
            if a in {"."}:
                countdot += 1
        if countexp > 1:
            return False
        if countsign > 2:
            return False
        if countdot > 1:
            return False


        def isinteger(s):
            for a in s:
                if a not in integerset:
                    return False
            return True

        def isdecimal(s):
            if "." in s:
                s = s.replace(".","")
            if len(s) == 0:
                return False
            return isinteger(s)

        if expi >= 0:
            if expi == n-1 or expi == 0:
                return False
            left = s[0:expi]
            right = s[expi+1:]
            # print(left,right)
            if left[0] in {"+","-"}:
                left = left[1:]
            if len(left) == 0:
                return False
            left = isinteger(left) or isdecimal(left)

            if right[0] in {"+","-"}:
                right = right[1:]
            if len(right) == 0:
                return False
            right = isinteger(right)
            return left and right     
        else:
            if s[0] in {"+","-"}:
                s = s[1:]
            if len(s) == 0:
                return False
            return isinteger(s) or isdecimal(s)
                
