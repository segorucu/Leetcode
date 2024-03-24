class Solution:
    def minOperations(self, k: int) -> int:
        
        minops = inf
        for i in range(1,k+1):
            additions = i-1
            multiplications = math.ceil(k/i)-1
            total = additions + multiplications
            minops = min(minops,total)
            
        return minops
        