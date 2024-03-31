class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        
        curr = numBottles
        rem = numBottles
        while rem >= numExchange:
            curr += 1
            rem = rem - numExchange
            rem += 1
            numExchange += 1
            
        return curr