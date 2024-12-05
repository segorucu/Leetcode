class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        n = len(start)
        arr1 = []
        for ch in start:
            if ch != "_":
                arr1.append(ch)
        arr2 = []
        for ch in target:
            if ch != "_":
                arr2.append(ch)
        if arr1[:] != arr2[:]:
            return False

        p1 = 0
        for p2,tar in enumerate(target):
            if tar == "_":
                continue
            while start[p1] == "_":
                p1 += 1
            if tar == "L":
                if p1 < p2:
                    return False
                else:
                    p1 += 1
            elif tar == "R":
                if p1 > p2:
                    return False
                else:
                    p1 += 1
            
            
            

        return True