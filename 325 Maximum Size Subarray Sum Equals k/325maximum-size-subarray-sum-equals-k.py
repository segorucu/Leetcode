from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        ans = 0
        
        table = defaultdict(list)
        table[0].append(0)

        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            table[sm].append(i+1)
            if sm - k in table:
                ans = max(ans,i+1-table[sm - k][0])


        return ans

        