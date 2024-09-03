class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:


        zeros = 0
        ones = 0
        l = r = 0
        n = len(s)
        ans = 0
        while r < n:
            if s[r] == "1":
                ones += 1
            else:
                zeros += 1
            r += 1
            while zeros > k and ones > k:
                if s[l] == "1":
                    ones -= 1
                else:
                    zeros -= 1
                l += 1
            ans += r-l

        return ans
        