class Solution:
    def numberOfWays(self, corridor: str) -> int:
        sums = 0 
        lastS = 0
        locs = []
        prevright = -1
        for i, c in enumerate(corridor):
            if c == 'S':
                sums += 1
                lastS = i
                if sums % 2 == 1:
                    left = i
                elif sums % 2 == 0:
                    right = i
                    locs.append((left,right))

        if sums % 2 == 1 or sums == 0:
            return 0
        if sums == 2:
            return 1

        n = len(locs)
        product = 1
        for i in range(n-1):
            gap = locs[i+1][0] - locs[i][1]
            product *= gap

        return product % (10**9+7)
        

        