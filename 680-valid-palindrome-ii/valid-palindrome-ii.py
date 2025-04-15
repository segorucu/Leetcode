class Solution:
    def ispalindrome(self, txt):
        m = len(txt)
        l = 0
        r = m-1
        while l < r:
            if txt[l] == txt[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:

        n = len(s)
        l = 0
        r = n-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                one = s[l+1:r+1]
                res1 = self.ispalindrome(one)
                two = s[l:r]
                res2 = self.ispalindrome(two)
                if res1 or res2:
                    return True
                return False

        return True
        
        

        
        return dp(0,n-1,1)
        