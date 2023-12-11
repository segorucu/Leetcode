class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        
        def backtrack(i,j,curr):
            if i == n and j == n:
                ans.append(curr)

            if i <= n:
                curr += "("
                backtrack(i+1,j,curr)
                curr = curr[:-1]

            if j < i:
                curr += ")"
                backtrack(i,j+1,curr)
                curr = curr[:-1]

        backtrack(0,0,"")
        return ans