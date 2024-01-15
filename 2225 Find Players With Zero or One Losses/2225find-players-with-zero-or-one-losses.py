class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        ones = set()
        mores = set()
        for winner, loser in matches:
            winners.add(winner)
            if loser not in ones and loser not in mores:
                ones.add(loser)
            else:
                mores.add(loser)
                if loser in ones:
                    ones.remove(loser)

        for winner, loser in matches:
            if loser in winners:
                winners.remove(loser)

        answer = [None, None]
        answer[0] = list(sorted(winners))
        answer[1] = list(sorted(ones))

        return answer
