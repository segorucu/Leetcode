class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        
        arr = []
        for i, hero in enumerate(heroes):
            arr.append((hero, i))
        arr.sort()

        arr2 = []
        for m, c in zip(monsters, coins):
            arr2.append((m, c))
        arr2.sort()

        n = len(heroes)
        ans = n * [0]
        l = 0
        sm = 0
        m = len(monsters)
        for hero, i in arr:
            while l < m and arr2[l][0] <= hero:
                sm += arr2[l][1]
                l += 1
            ans[i] = sm
        return ans
