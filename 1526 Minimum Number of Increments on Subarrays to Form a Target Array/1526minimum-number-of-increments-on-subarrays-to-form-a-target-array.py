class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        ops = target[0]
        incr = 0
        n = len(target)
        for i in range(1,n):
            if target[i-1] < target[i]:
                ops += target[i] - target[i-1]

        return ops 