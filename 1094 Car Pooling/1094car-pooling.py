class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        stack = []
        for num, source, to in(trips):
            stack.append([source,num])
            stack.append([to,-num])
            if num > capacity:
                return False

        stack.sort()
        n = len(stack)
        tot = 0
        for _, people in stack:
            tot += people
            if tot > capacity:
                return False
            

        return True
