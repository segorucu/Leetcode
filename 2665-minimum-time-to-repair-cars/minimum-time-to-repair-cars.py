class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        left = 1
        right = min(ranks) * cars ** 2
        
        def good(val):
            tot = 0
            for num in ranks:
                tot += int((val/num)**0.5)
            # print()
            return tot >= cars

        res = 0
        while left <= right:
            mid = (left + right) // 2
            if good(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1


        return res