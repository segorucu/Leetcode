class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        
        def check(word,original):
            for a,b in zip(word,original):
                if a != b and a != "*":
                    return False
            return True
        
        original = word
        it = 0
        while True:
            word = word[k:]
            word += k*"*"
            it += 1
            if check(word,original):
                return it
            
        
        return 0