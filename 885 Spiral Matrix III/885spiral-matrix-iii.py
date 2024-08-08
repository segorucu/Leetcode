class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        def valid(currow,curcol):
            return 0 <= currow < rows and 0 <= curcol < cols
        Nrow = Srow = rStart
        Wcol = cStart
        Ecol = cStart + 1
        ans = []
        size = rows * cols
        currow = rStart
        curcol = cStart
        direction = "E"
        while len(ans) < size:
            if direction == "E":
                while curcol <= Ecol:
                    if valid(currow,curcol):
                        ans.append([currow,curcol])
                    curcol += 1
                curcol -= 1
                currow += 1
                direction = "S" 
                Srow += 1
            elif direction == "S":
                while currow <= Srow:
                    if valid(currow,curcol):
                        ans.append([currow,curcol])
                    currow += 1
                currow -= 1
                curcol -= 1
                direction = "W"
                Wcol -= 1
            elif direction == "W":
                while curcol >= Wcol:
                    if valid(currow,curcol):
                        ans.append([currow,curcol])
                    curcol -= 1
                curcol += 1
                currow -= 1
                direction = "N"
                Nrow -= 1
            elif direction == "N":
                while currow >= Nrow:
                    if valid(currow,curcol):
                        ans.append([currow,curcol])
                    currow -= 1
                currow += 1
                curcol += 1
                direction = "E"
                Ecol += 1

        return ans

        