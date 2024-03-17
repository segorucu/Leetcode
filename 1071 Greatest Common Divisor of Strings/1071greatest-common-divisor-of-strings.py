class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def check(text, sub):
            k = len(sub)
            n = len(text) // k
            for i in range(n):
                beg = i * k
                end  = beg + k
                if text[beg:end] != sub:
                    return False
            return True

        n, m = len(str1), len(str2)
        if m > n:
            str1, str2 = str2, str1
            m, n = n, m

        checked = set()
        ans = ""
        for i in range(m):
            cand = str2[0:i+1] 
            if cand not in checked and m % len(cand) == 0 and n % len(cand) == 0 and check(str1,cand) and check(str2,cand):
                if len(ans) < len(cand):
                    ans = cand
            checked.add(cand)
        return ans
