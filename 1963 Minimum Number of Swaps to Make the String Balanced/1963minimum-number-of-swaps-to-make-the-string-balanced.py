class Solution:
    def minSwaps(self, s: str) -> int:
 
        
        n = len(s)
        l = 0
        r = n-1
        s = list(s)
        arr = []
        missing = 0
        open = 0
        for a in s:
            if a == "[":
                open += 1
            else:
                if open:
                    open -= 1
                else:
                    missing += 1
        return (missing+1) // 2