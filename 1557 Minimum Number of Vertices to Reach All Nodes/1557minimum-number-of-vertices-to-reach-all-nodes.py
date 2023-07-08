class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for _, j in edges:
            indegree[j] += 1

        ans = [i for i in range(n) if indegree[i] == 0]

        return ans