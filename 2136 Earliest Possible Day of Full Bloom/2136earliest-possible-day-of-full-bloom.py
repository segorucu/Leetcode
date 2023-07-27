class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        maxHeap = [(growTime[i],plantTime[i]) for i in range(len(plantTime))]
        maxHeap.sort(key = lambda x : -x[0])

        growing = 0
        sm = 0
        for g,p in maxHeap:
            growing = max(g,growing-p)
            sm += p

        return sm + growing