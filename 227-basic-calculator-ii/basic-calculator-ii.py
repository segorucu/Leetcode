class Solution:
    def calculate(self, s: str) -> int:
        
        s = list(s)
        stack = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
            else:
                if not s[i].isnumeric():
                    stack.append(s[i])
                    i += 1
                else:
                    curr = ""
                    while i < len(s) and s[i].isnumeric():
                        curr += s[i]
                        i += 1
                    stack.append(curr)

        s = stack.copy()

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
                    if s[i] == "*":
                        left = stack.pop()
                        right = s[i+1]
                        curr = int(left) * int(right)
                        stack.append(curr)
                        i += 2
                    else:
                        left = stack.pop()
                        right = s[i+1]
                        curr = int(left) // int(right)
                        stack.append(curr)
                        i += 2
            return stack

        s = multiplyanddivide(s)

       
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if i == 0:
                if s[i] == "-":
                    sm = -int(s[i+1])
                    i += 2
                else:
                    sm = int(s[i])
                    i += 1
            else:
                if s[i] == "+":
                    sm += int(s[i+1])
                else:
                    sm -= int(s[i+1])
                i += 2

        return sm