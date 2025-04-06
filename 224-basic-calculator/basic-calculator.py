class Solution:
    def calculate(self, s: str) -> int:
        
        ops = {"+": 1, "-": -1}
        digits = set("0123456789")
        s = s.replace(" ","")
        n = len(s)

        arr = []
        i = 0
        while i < n:
            if s[i] in {"(",")"}:
                arr.append(s[i])
                i += 1
            else:
                if i < n-1 and s[i+1] == "(":
                    arr.append(s[i:i+2])
                    i += 2
                    continue
                mult = 1
                if s[i] in ops:
                    mult = ops[s[i]]
                    i += 1
                beg = i
                while i < n and s[i] in digits:
                    i += 1
                curr = int(s[beg:i]) * mult
                arr.append(curr)

        stack = [1]
        res = 0
        for c in arr:
            if c == "+(" or c == "(":
                stack.append(stack[-1])
            elif c == "-(":
                stack.append(-stack[-1])
            elif c == ")":
                stack.pop()
            else:
                res += stack[-1] * c

        return res
            

