class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        

        nloops = n // 2
        left = top = 0
        right = bottom = n-1
        ans = [n*[0] for _ in range(n)]
        count = 0
        for loop in range(nloops):
            for j in range(left,right+1):
                count += 1
                ans[top][j] = count
            top += 1
            for i in range(top,bottom+1):
                count += 1
                ans[i][right] = count
            right -= 1
            for j in range(right,left-1,-1):
                count += 1
                ans[bottom][j] = count
            bottom -= 1
            for i in range(bottom,top-1,-1):
                count += 1
                ans[i][left] = count
            left += 1

        if n % 2 == 1:
            ans[left][top] =count + 1
        return ans


