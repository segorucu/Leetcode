class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        
        mp = collections.defaultdict(dict)

        for player, ball in pick:
            if ball not in mp[player]:
                mp[player][ball] = 1
            else:
                mp[player][ball] += 1

        ans = 0
        for i in range(n):
            if i in mp and max(mp[i].values()) > i:
                ans += 1

        return ans
