class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        # cost1 >= cost2


        sm = 0
        while total >= cost1:
            sm += (total // cost2 + 1)
            total -= cost1

        sm += total // cost2 + 1
        return sm