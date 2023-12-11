class Solution:
    def isValid(self, s: str) -> bool:
        close = {')': '(', '}': '{', ']': '['}
        opening = {"(","{","["}

        if len(s) % 2 == 1:
            return False

        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if close[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        

        


        return True
