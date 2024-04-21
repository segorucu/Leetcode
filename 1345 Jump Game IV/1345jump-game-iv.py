class Solution:
    def minJumps(self, arr: List[int]) -> int:

        graph = collections.defaultdict(set)
        n = len(arr)
        for i,a in enumerate(arr):
            graph[a].add(i)

        queue = set()
        queue.add(0)
        visited = set()
        visited.add(0)
        step = 0
        while queue:
            nex = set()
            if n-1 in queue:
                return step

            for node in queue:
                for neigh in graph[arr[node]]:
                    if neigh not in visited:
                        visited.add(neigh)
                        nex.add(neigh)
                del graph[arr[node]]

                for neigh in [node-1,node+1]:
                    if neigh not in visited and 0 <= neigh < n:
                        visited.add(neigh)
                        nex.add(neigh)  
            
            queue = nex 
            step += 1           

        return -1
        