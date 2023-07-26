class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        heapq.heapify(costs)

        ans = 0
        while costs:
            c = heapq.heappop(costs)
            coins -= c
            if coins < 0:
                return ans
            elif coins == 0:
                return ans + 1
            ans += 1

        return ans