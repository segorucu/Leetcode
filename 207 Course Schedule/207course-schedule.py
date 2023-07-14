from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        inDegree = [0]*numCourses
        forward = defaultdict(list)
        for course, prereq in prerequisites:
            forward[prereq].append(course)
            inDegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if inDegree[i]==0:
                queue.append(i)

        opened = 0
        while queue:
            node = queue.popleft()
            opened += 1
            for neigh in forward[node]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    queue.append(neigh)

        return opened == numCourses

        