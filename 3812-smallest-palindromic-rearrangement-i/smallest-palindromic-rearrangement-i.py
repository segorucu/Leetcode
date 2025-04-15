class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        counter = Counter(s)

        ans = []
        odd = ""
        for k,v in counter.items():
            if v % 2:
                odd = k

            ans.extend((v//2) * k)

        ans.sort()
        ans = ans + [odd] + ans[::-1]
        return "".join(ans)
