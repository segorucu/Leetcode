class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        L = (n+1) * [0]
        L[n] = 0
        for i in range(n-1,-1,-1):
            j = i + questions[i][1] + 1
            j = min(j,n)
            L[i] = max(L[j]+questions[i][0],L[i+1])
    
        return L[0]