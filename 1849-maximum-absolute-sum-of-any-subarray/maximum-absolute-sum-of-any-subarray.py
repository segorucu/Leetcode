from sortedcontainers import SortedList
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        seen = SortedList()
        n = len(prefix)
        seen.add(0)
        ans = 0
        for i in range(1,n):
            seen.add(prefix[i])
            ans = max(ans, abs(seen[-1]-seen[0]))

        return ans


        