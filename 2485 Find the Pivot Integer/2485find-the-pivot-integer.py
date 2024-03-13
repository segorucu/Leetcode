class Solution:
    def pivotInteger(self, n: int) -> int:
        

        tot = n * (n+1) // 2 
        for i in range(1,n+1):
            left = i*(i+1) // 2
            right = tot - left + i
            if left == right:
                return i
        return -1