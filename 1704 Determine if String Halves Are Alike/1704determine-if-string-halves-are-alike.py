class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        mid = len(s) // 2
        a = b = 0
        for i,c in enumerate(s):
            if c in vowels:
                if i < mid:
                    a += 1
                else:
                    b += 1
        return a == b

        