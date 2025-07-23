class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        

        def removeba(s):
            stack = []
            ret = 0
            for char in s:
                if stack and char == "a" and stack[-1] == "b":
                    stack.pop()
                    ret += y
                else:
                    stack.append(char)
            s = "".join(stack)
            return ret, s

        def removeab(s):
            stack = []
            ret = 0
            for char in s:
                if stack and char == "b" and stack[-1] == "a":
                    stack.pop()
                    ret += x
                else:
                    stack.append(char)
            s = "".join(stack)
            return ret, s

        ans = 0
        if y >= x:
            ret, s = removeba(s)
            ans += ret
            ret, s = removeab(s)
            ans += ret
        else:
            ret, s = removeab(s)
            ans += ret
            ret, s = removeba(s)
            ans += ret

        return ans
            