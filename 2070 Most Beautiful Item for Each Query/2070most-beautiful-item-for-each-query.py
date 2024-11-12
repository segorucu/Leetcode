from sortedcontainers import SortedSet, SortedList
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort()

        # prices = SortedList()
        # for price, beauty in items:
        #     ind = prices.bisect_left((price,))
        #     if ind < len(prices) and prices[ind][0] == price:
        #         if beauty > prices[ind][1]:
        #             prices.pop(ind)
        #             prices.add((price, beauty))
        #     else:
        #         prices.add((price, beauty))
            
        arr = []
        for i,q in enumerate(queries):
            arr.append((q,i))

        arr.sort()
        n = len(queries)
        ans = n * [0]
        curr = 0
        l = 0
        for q,i in arr:
            while l < len(items) and items[l][0] <= q:
                curr = max(curr, items[l][1])
                l += 1 
            ans[i] = curr

        return ans