class Solution:
    def totalNQueens(self, n: int) -> int:

        ans = []
        usedrows = set()
        def backtrack(col,total,curr):
            if col == n:
                ans.append(curr[:])
                return 

            for row in range(n):
                if row in usedrows:
                    continue
                hit = False
                for cross in range(1,min(row,col)+1):
                    rown = row - cross
                    coln = col - cross
                    if curr[rown][coln] == "Q":
                        hit = True
                        break
                if hit:
                    continue
                for cross in range(1,min(n-row-1,col)+1):
                    rown = row + cross
                    coln = col - cross
                    if curr[rown][coln] == "Q":
                        hit = True
                        break
                if hit:
                    continue
                usedrows.add(row)
                store = curr[row]
                curr[row] = col*"." +"Q" +(n-col-1)*"."
                backtrack(col+1,total+1,curr)
                usedrows.remove(row)
                curr[row] = store

            return 


#   curr is the row number of each.
        curr = [n*"." for _ in range(n)]
        backtrack(0,0,curr)
        return len(ans)
        