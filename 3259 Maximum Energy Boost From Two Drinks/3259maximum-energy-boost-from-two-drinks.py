from functools import cache
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        
        n = len(energyDrinkA)

        @cache
        def dp(i,curr):
            if i == n:
                return 0

            if curr == "A":
                one = energyDrinkA[i] + dp(i+1,curr)
                two = dp(i+1,"B")
            elif curr == "B":
                one = energyDrinkB[i] + dp(i+1,curr)
                two = dp(i+1,"A")
            return max(one,two)



        return max(dp(0,"A"),dp(0,"B"))