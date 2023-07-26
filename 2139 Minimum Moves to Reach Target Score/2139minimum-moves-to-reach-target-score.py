class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        ops = 0
        while target > 1:
            if target % 2 == 1:
                target -= 1
                ops += 1
            if maxDoubles > 0:
                target /= 2
                target = int(target)
                ops += 1
                maxDoubles -= 1
            else:
                ops += target - 1
                break
        
        return ops