from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        counter = defaultdict(int)
        def validmove(pt):
            if len(counter) <= 1:
                return True
            elif len(counter) == 2 and s[pt] in counter:
                return True
            else:
                return False
        
        left = right = 0
        ans = 0
        while right < len(s):
            if validmove(right):
                counter[s[right]] += 1
                right += 1
            else:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            ans = max(ans,right-left)

        return ans

        