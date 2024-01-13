class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        s = " ".join(s)
        # print(s)

        return s
        