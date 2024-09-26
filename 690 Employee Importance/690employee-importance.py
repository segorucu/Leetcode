"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph = collections.defaultdict(list)
        importance_graph = collections.defaultdict(int)
        for employee in employees:
            e_id = employee.id
            graph[employee.id].extend(employee.subordinates)
            importance_graph[e_id] = employee.importance

        queue = collections.deque()
        queue.append(id)
        ans = 0
        while queue:
            id = queue.popleft()
            ans += importance_graph[id]
            for child in graph[id]:
                queue.append(child)



        return ans
        