class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        

        stack = []
        for char in s:
            # decide whether to append or modify
            if stack and stack[-1][0] == char:
                    stack[-1] = (stack[-1][0], stack[-1][1] + 1)
            else:
                stack.append((char,1))

            if stack[-1][1] == k:
                stack.pop()
        
        ans = []
        for k,v in stack:
            ans.append(v*k)

        return "".join(ans)
            