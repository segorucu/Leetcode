class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        
        # upper left
        start = [(0,0),(1,0),(0,1),(1,1)]
        for si, sj in start:
            whites = 0
            for i in range(2):
                for j in range(2):
                    if grid[si+i][sj+j] == "W":
                        whites += 1
            # print(whites)
            if whites != 2:
                return True
        return False