class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        

        def converttoint(num):
            curr = 0
            for a in num:
                curr = curr*10 + int(a)
            return curr

        sm = converttoint(num1) + converttoint(num2)
        if sm == 0: return "0"
        ans = []
        while sm:
            ans.append(str(sm%10))
            sm = sm // 10

        ans.reverse()
        return "".join(ans)
