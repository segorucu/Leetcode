from functools import cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        start = locations[start]
        finish = locations[finish]
        if abs(start-finish) > fuel:
            return 0

        MOD = 10**9+7
        locations.sort()
        n = len(locations)
        @cache
        def dp(prev,fuel):
            count = 0
            if prev == finish:
                count =  1

            for loc in locations:
                if loc == prev:
                    continue
                rem = fuel - abs(prev-loc)
                if rem >= 0:
                    count += dp(loc, rem) % MOD

            return count % MOD


        return dp(start,fuel)
        