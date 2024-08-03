class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        cardset = set(fronts)
        cardset.update(backs)

        for f,b in zip(fronts,backs):
            if f == b and f in cardset:
                cardset.remove(f)

        if len(cardset) == 0:
            return 0
        return min(cardset)
        