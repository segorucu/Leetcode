class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        arr = []
        add = 0
        open = 0
        for a in s:
            if a == "(":
                open += 1
            else:
                if open:
                    open -= 1
                else:
                    add += 1

        return add + open
