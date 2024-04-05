class Solution:
    def makeGood(self, s: str) -> str:
        
        # print(ord("a")-ord("A"))
        
        stack = []
        for c in s:
            if stack and abs(ord(stack[-1])-ord(c)) == 32:
                    stack.pop()
            else:
                stack.append(c)

        
        return "".join(stack)
        