from heapq import heapify, heappop, heappush
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        stack = []
        for i,(a,b) in enumerate(tasks):
            stack.append((a,b,i))
        stack.sort()
        # print(stack)
        currtime = stack[0][0]
        heap = []
        heappush(heap, (stack[0][1], stack[0][2], stack[0][0]))
        n = len(tasks)
        ans = []
        for i, cpu in enumerate(stack[1:],1):
   
            while currtime < cpu[0] and heap:
                    process, ind, enqueue = heappop(heap)
                    ans.append(ind)
                    currtime = max(currtime,enqueue) + process

            heappush(heap,(cpu[1], cpu[2], cpu[0]))

        while heap:
            process, ind, enqueue = heappop(heap)
            ans.append(ind)

        return ans





        return []
        