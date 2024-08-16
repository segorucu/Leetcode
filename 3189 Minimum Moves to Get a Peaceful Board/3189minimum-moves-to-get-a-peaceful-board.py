class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:

        rooks.sort()
        n = len(rooks)
        ans = 0
        for i, rook in enumerate(rooks):
            ans += abs(rook[0]-i)

        rooks.sort(key = lambda x: x[1])
        for j, rook in enumerate(rooks):
            ans += abs(rook[1]-j)


        return ans

        