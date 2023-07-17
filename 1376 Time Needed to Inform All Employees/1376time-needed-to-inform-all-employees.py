from collections import defaultdict, deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        adj = defaultdict(list)
        for employee, manager in enumerate(manager):
            if manager == -1:
                continue
            adj[manager].append(employee)

        queue = deque()
        queue.append((headID,0))

        maxtime = 0
        while queue:
            node, time = queue.popleft()
            maxtime = max(maxtime,time)
            dt = informTime[node]
            for neigh in adj[node]:
                queue.append((neigh,time+dt))


        return maxtime
