class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        n = len(shifts)
        prefix = n * [0]
        prefix[-1] = shifts[-1]
        for i in range(n-2,-1,-1):
            prefix[i] = prefix[i+1] + shifts[i]
            prefix[i] = prefix[i] % 26

        # print(prefix)
        ans = []
        base = ord("a")
        for i,a in enumerate(s):
            tot = (ord(a) - ord("a") + prefix[i]) % 26
            ans.append(chr(ord("a") + tot))

        return "".join(ans)
        
        