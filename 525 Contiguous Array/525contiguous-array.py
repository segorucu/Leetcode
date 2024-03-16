from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
          return 0
        sm = 0
        tab = defaultdict(int)
        tab[0] = 1
        ans = 0
        for i, num in enumerate(nums):
          if num == 1:
            sm += 1
          else:
            sm -= 1
          if tab[sm]:
            ans = max(ans,i+2-tab[sm])
          else:
            tab[sm] = i + 2
        
        return ans

        