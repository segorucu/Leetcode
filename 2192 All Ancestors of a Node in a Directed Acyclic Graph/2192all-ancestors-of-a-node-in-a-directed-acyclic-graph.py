from collections import defaultdict, deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ingoing = [0] * n
        adj = defaultdict(list)
        for parent, child in edges:
            adj[parent].append(child)
            ingoing[child] += 1

        queue = deque()
        visited = set()
        for i in range(n):
            if ingoing[i] == 0:
                queue.append(i)
                visited.add(i)

        ans = [set() for i in range(n)]
        while queue:
            node = queue.popleft()
            for neigh in adj[node]:
                ans[neigh].add(node)
                ans[neigh].update(ans[node])
                ingoing[neigh] -= 1
                if ingoing[neigh] == 0:
                    queue.append(neigh)

        for i in range(n):
            ans[i] = sorted(list(ans[i]))
        return ans



        

        return ans
