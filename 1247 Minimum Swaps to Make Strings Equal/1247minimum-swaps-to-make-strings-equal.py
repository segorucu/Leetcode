class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        xy = yx = 0
        for a,b in zip(s1,s2):
            if a != b:
                if a == "x":
                    xy += 1
                else:
                    yx += 1

        if (xy+yx) & 1:
            return -1 

        return xy // 2 + yx // 2 + int(xy & 1) + int(yx & 1)

        



        return 0