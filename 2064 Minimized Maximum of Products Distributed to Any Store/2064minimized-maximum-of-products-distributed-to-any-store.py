from bisect import bisect
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        minx = math.ceil(sum(quantities)/n)
        maxx = max(quantities)
        # print(minx, maxx)

        def candistribute(val):
            count = 0
            for q in quantities:
                count += math.ceil(q / val)
            return count <= n

        left = min(minx,maxx)
        right = max(minx,maxx)
        if left == right: 
            return left
        while left < right:
            mid = (left + right) // 2
            if candistribute(mid):
                right = mid
            else:
                left = mid + 1

        return right
        