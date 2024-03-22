class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {"e","o","a","i","u"}

        ans = []
        for a in s:
            if a not in vowels:
                ans.append(a)

        return "".join(ans)