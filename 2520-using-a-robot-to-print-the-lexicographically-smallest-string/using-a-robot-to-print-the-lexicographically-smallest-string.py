class Solution:
    def robotWithString(self, s: str) -> str:
        
        letters = list(set(s))
        letters.sort()
        s = list(s)
        minstack = deque()
        for i,a in enumerate(s):
            while minstack and minstack[-1][0] > a:
                minstack.pop()
            minstack.append((a,i))
        # print(minstack)
        stack = []
        t = []
        p = []
        i = 0
        while minstack:
            minletter, ind = minstack.popleft()
            if not t or t[-1] > minletter:
                t.extend(s[i:ind+1])
                i = ind+1
            while minstack and t and t[-1] <= minstack[0][0]:
                p.append(t.pop())
            # print(minstack, minletter, ind, s, p)
 
        t.reverse()
        p.extend(t)

        return "".join(p)

        # bacshdbrhphnwgir
        # s = ir
        # t = cshrhphnwg
        # p = abbd