class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        right = sum(weights)
        left = max(weights)

        def go(daily_capacity):
            day = 0
            curr = 0
            for weight in weights:
                if curr + weight > daily_capacity:
                    day += 1
                    curr = weight
                else:
                    curr += weight
                if day > days:
                    return False
            if curr:
                day += 1
            return day <= days
        
        while left <= right:
            mid = (left + right) // 2
            if go(mid):
                ret = mid
                right = mid -1
            else:
                left = mid + 1

        return ret