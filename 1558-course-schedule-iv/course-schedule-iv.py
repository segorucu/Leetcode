class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        preqgraph = collections.defaultdict(list)

        for preq, course in prerequisites:
            preqgraph[course].append(preq)

        fulllist = collections.defaultdict(set)

        def dfs(node,parent):
            for neigh in preqgraph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    fulllist[parent].add(neigh)
                    dfs(neigh,parent)

        for node in range(numCourses):
            visited = set()
            visited.add(node)
            dfs(node,node)

        ans = []
        for preq,course in queries:
            if preq in fulllist[course]:
                ans.append(True)
            else:
                ans.append(False)

        return ans