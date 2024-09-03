class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        base = ord("a")-1
        curr = []
        for a in s:
            curr.append(str(ord(a) - base))
        curr = "".join(curr)
        curr = int(curr)

        while k > 0:
            sm = 0
            while curr > 0:
                sm += (curr%10)
                curr = curr // 10
            curr = sm
            k -=1

        return curr
