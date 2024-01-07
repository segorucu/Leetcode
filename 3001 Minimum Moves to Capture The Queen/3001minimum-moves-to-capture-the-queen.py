class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        
        if a == e:
            if a == c and (b < d < f or f < d < b):
                rook = 2
            else:
                rook = 1
        elif b == f:
            if b == d and (a < c < e or e < c < a):
                rook = 2
            else:
                rook = 1
        else:
            rook = 2
            
        if abs(c-e) == abs(d-f):
            if abs(a-c) == abs(b-d) and abs(a-e) == abs(b-f) and (c<a<e or e<a<c) and (d<b<f or f<b<d):
                queen = 2
            else:
                queen = 1
        else:
            queen = 10
            
        # print(rook,queen)
            
        return min(rook,queen)
                