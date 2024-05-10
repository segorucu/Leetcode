class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        
        counter1 = collections.Counter(ranks)
        counter2 = collections.Counter(suits)

        if max(counter2.values()) >= 5:
            return "Flush"

        if max(counter1.values()) >= 3:
            return "Three of a Kind"

        if max(counter1.values()) >= 2:
            return "Pair"

        return "High Card"

        