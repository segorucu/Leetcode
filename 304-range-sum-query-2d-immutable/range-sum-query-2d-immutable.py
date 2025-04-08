class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix = [n*[0] for _ in range(m)]
        for r in range(m):
            prev = 0
            for c in range(n):
                prev += matrix[r][c]
                self.prefix[r][c] = self.prefix[r-1][c] + prev
        # print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        sm = self.prefix[row2][col2]
        if row1 > 0 and col1 > 0:
            sm += self.prefix[row1-1][col1-1]
        if row1 > 0:
            sm -= self.prefix[row1-1][col2]  
        # print(sm)  
        if col1 > 0:
            sm -= self.prefix[row2][col1-1]

        return sm



        return
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)