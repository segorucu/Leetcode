class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        sm = 0
        for i in range(n+1):
            if i % m:
                sm += i
            else:
                sm -= i

        return sm