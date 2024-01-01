class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [[1]]

        for row in range(1,numRows):
            temp = [1]
            for i in range(len(ans[row-1])-1):
                temp.append(ans[row-1][i] + ans[row-1][i+1])
            temp.append(1)
            ans.append(temp)

        return ans 