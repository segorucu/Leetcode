class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        MOD = 10**9+7
        ypoints = defaultdict(int)
        for x, y in points:
            ypoints[y] += 1

        print(ypoints)

        permutations = 0
        ans = 0
        for y, x in ypoints.items():
            if x > 1:
                curr = (x-1) * x // 2
                ans += permutations * curr
                ans = ans % MOD
                permutations += curr
                # permutations = permutations % MOD


        return ans 
