class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        banned = {"2", "3", "4", "5", "7"}
        for char in num:
            if char in banned:
                return False

        n = len(num)
        if n % 2:
            if num[n//2] not in {"0", "1", "8"}:
                return False

        reverse = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        l = 0
        r = n - 1
        while l < r:
            if num[l] != reverse[num[r]]:
                return False
            l += 1
            r -= 1

        return True


        return
        