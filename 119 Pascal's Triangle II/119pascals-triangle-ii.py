class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        prev = [1]
        if rowIndex == 0:
            return prev

        for _ in range(rowIndex):
            temp = [1]
            for i in range(len(prev)-1):
                temp.append(prev[i] + prev[i+1])
            temp.append(1)
            prev = temp

        return temp
        