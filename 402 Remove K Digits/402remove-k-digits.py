class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        

        stack = []
        i = 0
        n = len(num)
        if k == n:
            return "0"
        rem = k
        while rem > 0:
            if stack and num[i] < stack[-1]:
                stack.pop()
                rem -= 1
                continue
            stack.append(num[i])
            i += 1
            if i == n:
                break
                
        while len(stack) > n - k:
            stack.pop()
        if len(stack) < n-k:
            for j in range(i,n):
                if len(stack) < n - k:
                    stack.append(num[j])
        beg = 0
        while stack and beg < len(stack) and stack[beg] == '0':
            beg += 1
        
        if len(stack[beg:]) == 0:
            return "0"
        return "".join(stack[beg:])

            
