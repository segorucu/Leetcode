class Solution:
    def calculate(self, s: str) -> int:
        
        s = s.replace(" ","")
        s = list(s)
        stack = []
        i = 0
        while i < len(s):
            if not s[i].isnumeric():
                stack.append(s[i])
                i += 1
            else:
                curr = []
                while i < len(s) and s[i].isnumeric():
                    curr.append(s[i])
                    i += 1
                stack.append("".join(curr))

        s = stack

        def multiplyanddivide(s):
            n = len(s)
            stack = []
            i = 0
            while i < n:
                if s[i] not in {"*","/"}:
                    if s[i].isnumeric():
                        s[i] = int(s[i])
                    stack.append(s[i])
                    i += 1
                else:
                    left = stack.pop()
                    right = s[i+1]
                    if s[i] == "*":
                        curr = int(left) * int(right)
                    else:
                        curr = int(left) // int(right)
                    stack.append(curr)
                    i += 2
            return stack

        s = multiplyanddivide(s)

        stack = []
        i = 0
        if s[i] == "-":
            sm = -int(s[i+1])
            i += 2
        else:
            sm = int(s[i])
            i += 1
            
        n = len(s)
        while i < n:
            if s[i] == "+":
                sm += int(s[i+1])
            else:
                sm -= int(s[i+1])
            i += 2

        return sm