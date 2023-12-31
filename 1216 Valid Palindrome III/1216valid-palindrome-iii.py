from functools import cache
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        if k >= len(s)-1:
            return True

        @cache
        def dp(left,right,j):
            if j > k:
                return False
            if left >= right: 
                return True
        
            if s[left] == s[right]:
                res = dp(left+1,right-1,j)
                return res
            else:
                l = dp(left+1,right,j+1)
                if l:
                    return True
                r = dp(left,right-1,j+1)
                return l or r

        return dp(0,len(s)-1,0)


        