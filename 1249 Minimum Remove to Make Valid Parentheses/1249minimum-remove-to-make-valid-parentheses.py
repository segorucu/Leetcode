class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        

        keep = []
        stack = []
        for i,val in enumerate(s):
            if stack and val == ")":
                sym, ind = stack.pop()
                keep.append((sym, ind))
                keep.append((val, i))
            if val not in {"(",")"}:
                keep.append((val, i))
            elif val == "(":
                stack.append((val, i))


        keep.sort(key = lambda x: x[1])
        ans = [keep[i][0] for i in range(len(keep)) ]

        return "".join(ans)

            