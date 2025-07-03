class Solution:
    def kthCharacter(self, k: int) -> str:
        

        txt = "a"
        while len(txt) < k:
            curr = ""
            for letter in txt:
                curr += chr(ord(letter)+1)
            txt += curr

        return txt[k-1]