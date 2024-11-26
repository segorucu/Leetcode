class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set(range(n))

        for a,b in edges:
            if b in visited:
                visited.remove(b)


        if len(visited) == 1:
            return list(visited)[0]
        return -1