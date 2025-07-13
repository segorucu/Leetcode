class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()
        ans = i = j = 0
        while i < len(players) and j < len(trainers):
            player = players[i]
            trainer = trainers[j]
            while player > trainer:
                j += 1
                if j >= len(trainers):
                    return ans
                trainer = trainers[j]
            ans += 1
            i += 1
            j += 1

        return ans