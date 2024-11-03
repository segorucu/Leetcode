class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        

        n = len(s)
        if len(s) != len(goal):
            return False

        for i in range(n):
            if s[i:] + s[0:i] == goal[:]:
                return True

        return False