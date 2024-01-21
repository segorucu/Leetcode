class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n= len(s)
        def dp(l,r,k):
            if l > r:
                return True

            dec = False
            if s[l] == s[r]:
                dec = dec or dp(l+1,r-1,k)
            elif k > 0:
                dec = dec or dp(l+1,r,0) or dp(l,r-1,0)
            return dec

        
        return dp(0,n-1,1)
        