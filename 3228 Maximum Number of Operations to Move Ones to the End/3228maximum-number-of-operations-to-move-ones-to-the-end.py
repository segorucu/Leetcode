class Solution:
    def maxOperations(self, s: str) -> int:
        
        s = s[::-1]
        s = list(s)
        print(s)

        ones = 0
        ans = 0
        while s:
            while s and s[-1] == "0":
                s.pop()
            while s and s[-1] == "1":
                s.pop()
                ones += 1
            else:
                if s:
                    ans += ones
                
        return ans