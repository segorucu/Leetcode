from functools import cache
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        m = len(students)
        n = len(students[0])

        calc = collections.defaultdict(int)
        for i in range(m):
            for j in range(m):
                curr = 0
                for q in range(n):
                    if students[i][q] == mentors[j][q]:
                        curr += 1
                calc[i,j] = curr

        visitedstudent = set()
        visitedmentor = set()
        ans = [0]
        def backtrack(ibeg,sm):
            if len(visitedmentor) == m:
                return sm

            res = 0
            for i in range(ibeg,m):
                for j in range(m):
                    if j not in visitedmentor:
                        visitedmentor.add(j)
                        cost = calc[i,j]
                        res = max(res,backtrack(i+1,sm+cost))
                        visitedmentor.remove(j)
            return res
                     
        
        return backtrack(0,0)