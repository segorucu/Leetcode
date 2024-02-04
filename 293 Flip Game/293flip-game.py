class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        ans = []
        n = len(currentState)
        for i in range(n-1):
            if currentState[i] == currentState[i+1] == "+":
                tmp = currentState[0:i] + "--" + currentState[i+2:]
                ans.append(tmp)

        return ans
        