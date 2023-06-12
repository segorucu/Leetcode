class Solution:
    def reverseWords(self, s: str) -> str:
        final = ""
        for word in s.split():
            final += word[::-1]
            final += " "

        return final[:-1]
            
