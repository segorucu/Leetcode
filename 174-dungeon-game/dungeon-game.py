class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        m = len(dungeon)
        n = len(dungeon[0])

        dungeon[-1][-1] = max(1,1-dungeon[-1][-1])
        for r in range(m-2,-1,-1):
            dungeon[r][-1] = max(1,dungeon[r+1][-1]-dungeon[r][-1])
        
        for c in range(n-2,-1,-1):
            dungeon[-1][c] = max(1,dungeon[-1][c+1]-dungeon[-1][c])
        # print(dungeon)
        for r in range(m-2,-1,-1):
            for c in range(n-2,-1,-1):
                dungeon[r][c] = max(1,
                                min(dungeon[r+1][c],dungeon[r][c+1])-dungeon[r][c])

        
        return dungeon[0][0]