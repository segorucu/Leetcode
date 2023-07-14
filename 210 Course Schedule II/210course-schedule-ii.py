from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        inDegree = [0] * numCourses
        forward = defaultdict(list)
        for course, pre in prerequisites:
            forward[pre].append(course)
            inDegree[course] += 1
            
        ans = []
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        tot = 0  
        while queue:
            node = queue.popleft()
            tot += 1
            ans.append(node)
            for neigh in forward[node]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    queue.append(neigh)
        
        if tot != numCourses:
            return []
                    
        return ans
                    
            
        