class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        arr.sort()
        visited = set()
        for a in arr:
            if a <= 0:
                if a*2 in visited:
                    return True
            elif a > 0:
                if a % 2 == 0 and (a // 2) in visited:
                    return True
            visited.add(a)

        return False 
