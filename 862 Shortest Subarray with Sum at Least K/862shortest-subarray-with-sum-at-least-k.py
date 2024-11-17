from sortedcontainers import SortedList
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        sm = 0
        res = inf
        q = collections.deque()
        for i, num in enumerate(nums):
            sm += num
            if sm >= k:
                res = min(res,i+1)

            while q and sm - q[0][0] >= k:
                val, ind = q.popleft()
                res = min(res, i-ind)

            while q and q[-1][0] >= sm:
                q.pop()
            q.append((sm,i))

        return -1 if res==inf else res