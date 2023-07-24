class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        asteroids.sort()
        for aster in asteroids:
            if mass >= aster:
                mass += aster
            else:
                return False

        return True
