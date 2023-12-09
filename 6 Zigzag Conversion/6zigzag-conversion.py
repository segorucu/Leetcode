class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s

        ans = []
        row = col = 0
        declining = True
        for i, c in enumerate(s):
            if row < numRows and declining:
                ans.append((row,col,c))
                row += 1
            elif row == numRows:
                declining = False
                (rowo, colo, _) = ans[-1]
                row = numRows - 2
                col = colo + 1
                ans.append((row,col,c))
            elif declining == False:
                (rowo, colo, _) = ans[-1]
                if rowo == 0:
                    declining = True
                    col = colo
                    row = rowo + 1
                    ans.append((row,col,c))
                    row += 1
                else:
                    row -= 1
                    col += 1
                    ans.append((row,col,c))

        ans = sorted(ans)
        
        final = ""
        for _, _, c in ans:
            final += c
        return final
                

