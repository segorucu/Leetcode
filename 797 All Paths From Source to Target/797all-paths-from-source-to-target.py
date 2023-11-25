class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        ans = []
        
        def backtrack(path):
            
            if path[-1] == n-1:
                ans.append(path[:])
                return
            
            for neigh in graph[path[-1]]:
                path.append(neigh)
                backtrack(path)
                path.pop()
                 
             
        backtrack([0])

        return ans
        