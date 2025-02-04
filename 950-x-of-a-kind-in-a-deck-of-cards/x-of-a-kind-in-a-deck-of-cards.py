class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        

        counter = Counter(deck)
        freqset = set(counter.values())
        if 1 in freqset:
            return False
        if len(freqset) == 1:
            return True

        return math.gcd(*freqset) > 1

        
        return False
         