from sortedcontainers import SortedList
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        
        queue = SortedList()
        for bulb in bulbs:
            queue.add(bulb)
            i = queue.index(bulb)
            n = len(queue)
            if i > 0 and queue[i] - queue[i-1] - 1 == k:
                return n
            if i < n-1 and queue[i+1] - queue[i] - 1 == k:
                return n

        return -1