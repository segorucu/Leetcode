class Solution:
    def minLength(self, s: str) -> int:
        
        newarr = []
        for val in s:
            if newarr and ((newarr[-1] == "A" and val == "B") or (newarr[-1] == "C" and val == "D")):
                newarr.pop()
            else:
                newarr.append(val)

        # print(newarr)
        return len(newarr)


