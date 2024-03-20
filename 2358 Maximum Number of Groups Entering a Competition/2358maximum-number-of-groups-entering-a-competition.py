class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        ans = 0
        n = len(grades)
        k = math.ceil(n*0.5)
        while k * (k+1) // 2 > n:
            k -= 1

        return k

