from sortedcontainers import SortedList
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        n = len(times)
        available = SortedList()
        available.update(list(range(0,n)))

        people = []
        for i, [b, e] in enumerate(times):
            people.append([b,e,i])
        people.sort(key = lambda x: x[0])

        occupied = SortedList()
        for beg, end, i in people:
            while occupied and occupied[0][0] <= beg:
                addin = occupied.pop(0)
                available.add(addin[1]) 
            minval = available.pop(0)
            occupied.add((end, minval))
            if i == targetFriend:
                return minval


        return 0
        
