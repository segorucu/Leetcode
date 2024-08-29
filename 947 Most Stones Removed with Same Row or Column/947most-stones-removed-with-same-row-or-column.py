class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        mp = collections.defaultdict(set)
        n = len(stones)

        for i in range(n):
            a = stones[i]
            for j in range(i+1,n):
                b = stones[j]
                if a[0] == b[0] or a[1] == b[1]:
                    mp[tuple(a)].add(tuple(b))
                    mp[tuple(b)].add(tuple(a))

        def explore(node):
            for neigh in mp[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    explore(neigh)


        visited = set()
        island = 0
        for stone in stones:
            stone = tuple(stone)
            if stone not in visited:
                visited.add(stone)
                explore(stone)
                island += 1
        

        return len(stones) - island
