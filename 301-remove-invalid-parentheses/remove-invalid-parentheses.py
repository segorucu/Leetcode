class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def valid(curr):
            stack = []
            for char in curr:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    if not stack:
                        return False
                    stack.pop()
            return len(stack) == 0

        ans = set()
        curr = []
        maxlen = [-1]
        n = len(s)
        def backtrack(i):
            if i == n:
                if valid(curr):
                    if len(curr) > maxlen[0]:
                        ans.clear()
                        ans.add("".join(curr))
                        maxlen[0] = len(curr)
                    elif len(curr) == maxlen[0]:
                        ans.add("".join(curr))
                return

            curr.append(s[i])
            backtrack(i+1)
            curr.pop()
            if s[i] in {"(",")"}:
                # omit
                backtrack(i+1)

        backtrack(0)
        return list(ans)

            



