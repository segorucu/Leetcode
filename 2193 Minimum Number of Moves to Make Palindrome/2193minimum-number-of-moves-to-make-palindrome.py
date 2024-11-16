class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        
        s = list(s)
        n = len(s)
        cost = 0
        while s:
            r = len(s)-1
            l = s.index(s[-1])
            if l == r:
                cost += r // 2
                s.pop()
            else:
                cost += l
                s.pop()
                s.pop(l)

        return cost




            

        return count