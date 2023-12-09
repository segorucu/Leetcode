class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        maxlen = 1
        ans = s[0]
        for i in range(n):
            left = i-1
            right = i+1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    if right - left + 1 > maxlen:
                        maxlen = right - left + 1
                        ans = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break

        for i in range(n):
            left = i-1
            right = i
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    if right - left + 1 > maxlen:
                        maxlen = right - left + 1
                        ans = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break

        return ans



        return ans




