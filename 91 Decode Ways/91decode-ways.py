class Solution:
    def numDecodings(self, s: str) -> int:
        def valid(c):
            if c[0] == "0":
                return False
            return 0 < int(c) <= 26

        prev = 1
        for i, c in enumerate(s):
            if i == 0:
                if c == "0":
                    return 0
                else:
                    last = 1
            else:
                sm = 0
                
                if valid(c):
                    sm += last
                if valid(s[i-1:i+1]):
                    sm += prev
                prev = last
                last = sm

        
        return last