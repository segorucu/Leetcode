class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        

        counter = Counter(deck)
        freqset = set(counter.values())
        if 1 in freqset:
            return False
        if len(freqset) == 1:
            return True

        minval = min(freqset)
        for div in range(2,minval+1):
            for val in freqset:
                if val % div:
                    break
            else:
                return True
        
        return False
         