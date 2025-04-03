class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)

        def ispalindrome(txt):
            l = 0
            r = len(txt)-1
            while l < r:
                if txt[l] != txt[r]:
                    return False
                l += 1
                r -= 1
            return True
                    
        ans = 1
        for i in range(n):
            for j in range(i,n+1):
                left = s[i:j]
                for k in range(m):
                    for m in range(k,m+1):
                        right = t[k:m]
                        if ispalindrome(left+right):
                            # print(left+right)
                            ans = max(ans, len(left+right))
        

        return ans
                