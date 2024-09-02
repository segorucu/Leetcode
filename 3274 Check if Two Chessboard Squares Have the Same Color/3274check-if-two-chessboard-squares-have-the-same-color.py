class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
        base = ord("a")-1
        r1,c1 = ord(coordinate1[0])-base, int(coordinate1[1])
        r2,c2 = ord(coordinate2[0])-base, int(coordinate2[1])

        if (r1 + c1) % 2 == (r2 + c2) % 2:
            return True
        else:
            return False