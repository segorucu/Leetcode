from heapq import heapify, heappush, heappop
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        n = len(classes)
        heap = []
        for p,t in classes:
            change =(p+1)/(t+1) - p/t
            heappush(heap,(-change,p,t))

        for _ in range(extraStudents):
            change, p, t = heappop(heap)
            p += 1
            t += 1
            change =(p+1)/(t+1) - p/t
            heappush(heap,(-change,p,t))

        average = 0
        for change, p, t in heap:
            average += p/t

        average = average / n
        return average


        return 0


        