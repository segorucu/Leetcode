class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        legalset = set(source)
        for val in target:
            if val not in legalset:
                return -1

        l2 = 0
        count = 0
        while l2 < len(target):

            for a in source:
                if l2 < len(target) and a == target[l2]:
                    l2 += 1

            count += 1
        return count
        

        return count

