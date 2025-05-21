class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        

        s = list(s)
        n = len(s)
        op = 0
        for i in range(n):
            if s[i] == "(":
                op += 1
            elif s[i] == ")":
                if op > 0:
                    op -= 1
                else:
                    s[i] = "*"

        op = 0
        for i in range(n-1,-1,-1):
            if s[i] == ")":
                op += 1
            elif s[i] == "(":
                if op > 0:
                    op -= 1
                else:
                    s[i] = "*"

        ans = []
        for i,a in enumerate(s):
            if a != "*":
                ans.append(a)

        return "".join(ans)

            