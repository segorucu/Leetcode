from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        counts = defaultdict(int)
        for c in text:
            counts[c] += 1
            
        balloon = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        ans = 100000
        for key, val in balloon.items():
            ans = min(ans, counts[key] // val)
            
        return ans
            
        