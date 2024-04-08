class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        queue = collections.deque()
        queue.extend(students)
        
        counter = collections.Counter(students)

        l = 0
        while queue:
            student = queue.popleft()
            if student == sandwiches[l]:
                l += 1
                counter[student] -= 1
            else:
                queue.append(student)
                if counter[sandwiches[l]] == 0:
                    break

        return len(queue)
