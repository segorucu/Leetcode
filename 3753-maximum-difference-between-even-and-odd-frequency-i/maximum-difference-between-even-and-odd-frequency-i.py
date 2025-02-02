class Solution:
    def maxDifference(self, s: str) -> int:
        
        counter = Counter(s)
        maxeven = maxodd =0
        mineven = minodd = 1000000

        for k,v in counter.items():
            if v % 2 == 0:
                maxeven = max(maxeven,v)
                mineven = min(mineven,v)
            else:
                maxodd = max(maxodd,v)
                minodd = min(minodd,v)

        return maxodd-mineven