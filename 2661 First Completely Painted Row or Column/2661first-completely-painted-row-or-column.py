class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        m = len(mat)
        n = len(mat[0])
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)

        for r in range(m):
            for c in range(n):
                rows[mat[r][c]] = r
                cols[mat[r][c]] = c


        totrows = collections.defaultdict(int)
        totcols = collections.defaultdict(int)
        for i,a in enumerate(arr):
            totrows[rows[a]] += 1
            totcols[cols[a]] += 1
            if totrows[rows[a]] == n or totcols[cols[a]] == m:
                return i




        