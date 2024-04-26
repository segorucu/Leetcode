from sortedcontainers import SortedList
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        prefix = SortedList()
        prefix.add(0)
        for num in nums:
            nxt = prefix[-1] + num
            if nxt > x:
                break
            prefix.add(nxt)
        m = len(prefix)

        postfix = [0]
        for num in nums[::-1]:
            nxt = postfix[-1] + num
            if nxt > x:
                break
            postfix.append(nxt)
        n = len(postfix)

        minval = inf
        for i in range(n):
            if i >= minval:
                break
            goal = x - postfix[i]
            try:
                ind = prefix.index(goal)
            except: 
                ind = -1
            # ind = bisect_left(prefix,goal)
            # print(j, ind)
            if ind > -1:
                minval = min(minval,i+ind)
        if minval > len(nums):
            return -1
        return minval
