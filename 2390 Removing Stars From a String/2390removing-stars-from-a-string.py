class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and c == "*":
                stack.pop()
            elif stack:
                stack.append(c)
            elif not stack and c != "*":
                stack.append(c)

        return "".join(stack)
            
