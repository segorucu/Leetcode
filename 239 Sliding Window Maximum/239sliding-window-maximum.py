from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = SortedList()
        ans = []
        for i, num in enumerate(nums):
            queue.add(num)
            if len(queue) == k:
                ans.append(queue[-1])
                tmp = nums[i-k+1]
                queue.remove(tmp)

        return ans

