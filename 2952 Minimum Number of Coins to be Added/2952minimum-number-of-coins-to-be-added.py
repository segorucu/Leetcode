class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        n = len(coins)
        coins.sort()
        ic = 0
        if coins[0] != 1:
            ans = 1
        else:
            ans = 0
            ic += 1
        
        covered = 1
        while covered < target:
            if ic < n and coins[ic] <= covered + 1:
                covered += coins[ic]
                ic += 1
            else:
                covered += covered + 1
                ans += 1
            

        return ans
        