from heapq import heapify, heappop, heappush
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        total = 0
        n = len(grid)
        last1mp = defaultdict()
        for r in range(n):
            last1 = -1
            for c in range(n):
                if grid[r][c] == 1:
                    last1 = c
            last1mp[r] = last1

        

        for r in range(n):
            if last1mp[r] <= r:
                continue
            for rp in range(r+1,n):
                if last1mp[rp] <= r:
                    break
            else:
                return -1

            total += rp - r
            for rn in range(rp,r,-1):
                last1mp[rn], last1mp[rn-1] = last1mp[rn-1], last1mp[rn]

                # print(last1mp)

        return total


