class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        start = curr = 0
        n = len(derived)
        for i in range(n):
            curr = curr ^ derived[i]

        return curr == start

