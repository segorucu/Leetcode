import heapq
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(cost) > sum(gas):
            return -1

        indices = []
        n = len(gas)
        for i in range(n):
            if gas[i] >= cost[i]:
                indices.append((cost[i]-gas[i],i))
        heapq.heapify(indices)


        while heapq:
            c, left = heapq.heappop(indices)
            # print(cost,cost[0])
            if gas[left] < cost[left]:
                left += 1
                continue
            loop = False
            right = left
            tank = 0
            while not loop:
                tank += gas[right] - cost[right]
                if tank < 0:
                    break
                right += 1
                right = right % n
                if right == left:
                    return left
            left += 1
        return -1