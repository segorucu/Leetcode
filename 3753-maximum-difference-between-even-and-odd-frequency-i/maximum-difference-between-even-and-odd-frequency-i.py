class Solution:
    def maxDifference(self, s: str) -> int:
        
        counter = Counter(s)
        maxodd =0
        mineven = 1000000

        for k,v in counter.items():
            if v % 2 == 0:
                mineven = min(mineven,v)
            else:
                maxodd = max(maxodd,v)

        return maxodd-mineven