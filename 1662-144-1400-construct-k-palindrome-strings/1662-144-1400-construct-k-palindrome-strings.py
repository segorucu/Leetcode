class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if len(s) < k:
            return False

        counter = collections.Counter(s)
        odds = 0
        for key, val in counter.items():
            if val % 2 == 1:
                odds += 1
        
        return odds <= k