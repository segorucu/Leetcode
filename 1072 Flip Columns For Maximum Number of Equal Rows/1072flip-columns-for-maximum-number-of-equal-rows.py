class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        c = collections.defaultdict(int)
        for r in matrix:
            c[tuple(r)] += 1
            rev = [1 - bit for bit in r]
            c[tuple(rev)] += 1


        return max(c.values())
        