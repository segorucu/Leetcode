from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def valid(node,move):
            new = node + move * arr[node]
            if 0 <= new < n:
                return new
            else:
                return -1

        if arr[start] == 0:
            return True

        n = len(arr)
        queue = deque()
        seen = set()
        queue.append(start)
        seen.add(start)

        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            for move in [-1,1]:
                new = valid(node,move)
                if new >= 0 and new not in seen:
                    seen.add(new)
                    queue.append(new)
        return False
