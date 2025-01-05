class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        ops = n * [0]
        for b,e,v  in shifts:
            if v == 0:
                ops[b] -= 1
                if e < n-1:
                    ops[e+1] += 1
            else:
                ops[b] += 1
                if e < n-1:
                    ops[e+1] -= 1

        curr = 0
        for i in range(1,n):
            ops[i] = ops[i-1] + ops[i]

        ans = n * [None]
        base = ord("a")
        for i in range(n):
            val = (ord(s[i]) - base + ops[i]) % 26
            val += base 
            ans[i] = chr(val)

        return "".join(ans)

                
        