class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        n = len(s)
        if n % 2 == 1:
            return False

        changeable = 0
        openpar = 0
        for i,(a, lock) in enumerate(zip(s,locked)):
            if lock == "0":
                changeable += 1
            else:
                if a == "(":
                    openpar += 1
                else:
                    if openpar > 0:
                        openpar -= 1
                    else:
                        if changeable == 0:
                            return False
                        changeable -= 1

        changeable = 0
        closepar = 0
        for i in range(n-1,-1,-1):
            a, lock = s[i], locked[i]
            if lock == "0":
                changeable += 1
            else:
                if a == ")":
                    closepar += 1
                else:
                    if closepar > 0:
                        closepar -= 1
                    else:
                        if changeable == 0:
                            return False
                        changeable -= 1

        return True
