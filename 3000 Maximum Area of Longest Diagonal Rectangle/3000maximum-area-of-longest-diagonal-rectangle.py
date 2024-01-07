class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longest = 0
        area = 0
        
        for a,b in dimensions:
            if a**2 + b** 2 > longest:
                longest = a**2 + b** 2
                area = a*b
            elif a**2 + b** 2 == longest:
                area = max(area,a*b)
                
        return area
                