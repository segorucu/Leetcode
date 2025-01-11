class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        if n <= 1:
            return n

        seen = set()
        left = 0
        right = 0
        ans = 0
        while right < n:
            c = s[right]
            if c not in seen:
                seen.add(c)
            else:
                while s[left] != c:
                    seen.remove(s[left])
                    left += 1
                left += 1
            right += 1
            ans = max(ans,right-left)
            
        return ans
        