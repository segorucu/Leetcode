class Solution:
    def solveEquation(self, equation: str) -> str:
        

        stack = []
        r = 0
        while r < len(equation):
            if equation[r] != "=":
                beg = r
                r += 1
                while r < len(equation) and equation[r] not in {"+","-","="}:
                    r += 1
                stack.append(equation[beg:r])
            else:
                stack.append(equation[r])
                r += 1
                

        totalx = 0
        totalnum = 0
        leftside = 1
        rightside = -1
        for val in stack:
            if val[-1] == "x":
                mult = 1
                if val[0] == "+":
                    mult = 1
                    val = val[1:]
                elif val[0] == "-":
                    mult = -1
                    val = val[1:]
                if len(val) > 1:
                    totalx += mult * leftside * int(val[0:-1])
                else:
                    totalx += mult* leftside
            elif val[-1].isdigit():
                totalnum += rightside * int(val)
            elif val == "=":
                leftside = -1
                rightside = 1

        if totalx == 0:
            if totalnum == 0:
                return "Infinite solutions"
            else:
                return "No solution"

        ans = totalnum // totalx

        return "x=" + str(ans)

