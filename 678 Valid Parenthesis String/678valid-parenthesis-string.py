from functools import cache
class Solution:
    def checkValidString(self, s: str) -> bool:

        @cache 
        def backtrack(i,op):
            if i == len(s):
                return op == 0

            if s[i] == "(":
                op += 1
                return backtrack(i+1,op)
            elif s[i] == ")":
                op -= 1
                if op >= 0:
                    return backtrack(i+1,op)
                else:
                    return False
            else:
                one = backtrack(i+1,op+1)
                two = backtrack(i+1,op)
                three = False
                if op > 0:
                    three = backtrack(i+1,op-1)
                return one or two or three

        return backtrack(0,0)

            