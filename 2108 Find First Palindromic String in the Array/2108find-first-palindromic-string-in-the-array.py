class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def ispalindromic(word):
            l = 0
            r = len(word)-1
            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        for word in words:
            if ispalindromic(word):
                return word

        return ""