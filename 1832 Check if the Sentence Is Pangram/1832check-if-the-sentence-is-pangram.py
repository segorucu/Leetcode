class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        st = set(sentence)
            
        return len(st) == 26
        
        