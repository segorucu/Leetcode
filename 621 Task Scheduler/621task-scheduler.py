class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        queue = sorted(collections.Counter(tasks).values(), reverse = True)
        
        ans = 0
        while queue and queue[0] > 1:
            for i in range(min(len(queue),n+1)):
                queue[i] -= 1
            ans += (n+1)
            queue.sort(reverse = True)
            while queue[-1] == 0:
                queue.pop()

        ans += len(queue)

        return ans

        