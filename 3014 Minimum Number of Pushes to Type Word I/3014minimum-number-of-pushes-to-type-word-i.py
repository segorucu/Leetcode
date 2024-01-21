class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = collections.Counter(word)
        modulus = 8
        total = 0
        count = 0
        for key, val in counter.items():
            add = count // modulus + 1
            count += 1
            total += add
            
            
        return total
        