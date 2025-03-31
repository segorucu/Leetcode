class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)
        n = len(mat[0])
        
        ans = []
        for i in range(n):
            curr = []
            c = i
            r = 0
            while c >= 0 and r < m:
                curr.append(mat[r][c])
                c -= 1
                r += 1
            ans.append(curr)

        for i in range(1,m):
            curr = []
            c = n-1
            r = i
            while c >= 0 and r < m:
                curr.append(mat[r][c])
                c -= 1
                r += 1
            ans.append(curr)

        final = []
        for i,curr in enumerate(ans):
            if i % 2 == 0:
                curr.reverse()
            final.extend(curr)
            
        return final
