class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        

        def longestone(arr):
            maxval = 0 
            for i,a in enumerate(arr):
                if i > 0 and arr[i] > 0:
                    arr[i] = arr[i-1]+1
                maxval = max(maxval, arr[i])
            return maxval

        m = len(mat)
        n = len(mat[0])
        ans = 0
        for r in range(m):
            ret = longestone(mat[r][:])
            ans = max(ans,ret)

        for c in range(n):
            arr = []
            for r in range(m):
                arr.append(mat[r][c])
            ret = longestone(arr)
            ans = max(ans,ret)
            
        for r in range(m-1,-1,-1):
            c = 0
            arr = []
            while r < m and c < n:
                arr.append(mat[r][c])
                r += 1
                c += 1
            ret = longestone(arr)
            ans = max(ans,ret)

        for c in range(1,n):
            r = 0
            arr = []
            while r < m and c < n:
                arr.append(mat[r][c])
                r += 1
                c += 1
            ret = longestone(arr)
            ans = max(ans,ret)

        for r in range(m):
            c = 0
            arr = []
            while r >= 0 and c < n:
                arr.append(mat[r][c])
                r -= 1
                c += 1
            ret = longestone(arr)
            ans = max(ans,ret)

        for c in range(1,n):
            r = m-1
            arr = []
            while r >= 0 and c < n:
                arr.append(mat[r][c])
                r -= 1
                c += 1
            ret = longestone(arr)
            ans = max(ans,ret)    

        return ans


