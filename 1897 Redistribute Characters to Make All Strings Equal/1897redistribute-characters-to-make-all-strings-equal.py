from collections import defaultdict
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        counter = defaultdict(int)
        for word in words:
            for a in word:
                counter[a] += 1

        n = len(words)
        for key,val in counter.items():
            if val % n != 0:
                return False

        return True


        