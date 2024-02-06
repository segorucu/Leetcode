class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        counter = collections.Counter(s)
        for key,val in counter.items():
            if val == 1:
                return s.index(key)

        return -1