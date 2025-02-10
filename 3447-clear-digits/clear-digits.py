class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []
        for a in s:
            if a.isdigit():
                stack.pop()
            else:
                stack.append(a)

        return "".join(stack)