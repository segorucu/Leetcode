class Solution:
    def decodeString(self, s: str) -> str:
        
        number = []
        parant = []
        stack = []
        r = 0
        n = len(s)
        while r < n:
            if s[r].isdigit():
                num = []
                while r < n and s[r].isdigit():
                    num.append(s[r])
                    r += 1
                number.append(int("".join(num)))
            elif s[r] == "[":
                parant.append(r)
                r += 1
            elif s[r] == "]":
                num = number.pop()
                left = parant.pop()
                curr = ""
                while stack and stack[-1][0] > left:
                    curr = stack.pop()[1] + curr
                stack.append((left, num * curr))
                r += 1
            else:
                stack.append((r,s[r]))
                r += 1

        ans = ""
        for i,t in stack:
            ans += t

        return ans