class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        

        arr = []
        MAXVAL = max(health)
        n = len(damage)
        currsum = sum(damage)
        for i in range(n):
            d = damage[i]
            h = health[i]
            days = math.ceil(h/power)
            damage_per_day = d / days
            arr.append((damage_per_day,days,d,i))

        arr.sort()
        ans = 0
        while arr:
            damage_per_day, days, d, i = arr.pop()
            ans += currsum * days
            currsum -= damage[i]


        return ans
