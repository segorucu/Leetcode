class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        s = list(s)
        n = len(s)

        left = 0
        right = n - 1

        while right > left:
            if s[left].isalpha() == False:
                left += 1
                continue
            if s[right].isalpha() == False:
                right -= 1
                continue
            dum = s[right]
            s[right] = s[left]
            s[left] = dum
            right -= 1
            left += 1

        s = ''.join(s)
        return s