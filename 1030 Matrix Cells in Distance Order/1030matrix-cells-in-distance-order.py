class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        arr = []
        for r in range(rows):
            for c in range(cols):
                dist = abs(r-rCenter) + abs(c-cCenter)
                arr.append((dist,r,c))

        arr.sort()

        ans = []
        for d,r,c in arr:
            ans.append([r,c])

        return ans
        