class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        p1 = len(a) - 1
        p2 = len(b) - 1
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry > 0:
            sm = 0
            if p1 >= 0:
                sm += int(a[p1])
                p1 -= 1
            if p2 >= 0:
                sm += int(b[p2])
                p2 -= 1
            sm += carry
            rem = sm % 2
            carry = sm // 2
            ans.append(str(rem))
        ans.reverse()

        return "".join(ans)

