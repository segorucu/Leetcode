class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        curr = 0
        for dr, amount in shift:
            if dr == 0:
                curr -= amount
            else:
                curr += amount
        n = len(s)
        curr = curr % n
        s = s[n-curr:n] + s[0:n-curr]
        return s
        