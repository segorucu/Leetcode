class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        

        enemyEnergies.sort()
        points = 0
        if currentEnergy >= enemyEnergies[0]:
            currentEnergy -= enemyEnergies[0]
            points += 1
        else:
            return 0

        while enemyEnergies:
            if currentEnergy >= enemyEnergies[0]:
                point = currentEnergy // enemyEnergies[0]
                currentEnergy -= enemyEnergies[0] * point
                points += point
            else:
                currentEnergy += enemyEnergies[-1]
                enemyEnergies.pop()

        return points

