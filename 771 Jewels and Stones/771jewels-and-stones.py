from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        ans = sum(1 for stone in stones if stone in jewels)
            
        return ans
        