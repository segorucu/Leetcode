class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        tot = 0
        for a in range(max(0,2-2*limit),limit+1):
            maxlimit = min(limit,n-a)
            minlimit = max(0,n-a-limit)
            # print(a,minlimit,maxlimit)
            if maxlimit >= minlimit >= 0:
                tot += maxlimit - minlimit + 1
            # if n-a <= limit:
            #     tot += 1

        return tot
        