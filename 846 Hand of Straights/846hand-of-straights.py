from sortedcontainers import SortedList
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)
        if n % groupSize != 0:
            return False

        groups = n // groupSize
        # counter = collections.Counter(hand)
        # hand.sort()
        arr = SortedList(hand)
        for _ in range(groups):
            prev = arr.pop(0)
            for _ in range(groupSize-1):
                nxt = prev + 1
                if arr.count(nxt) > 0:
                    arr.remove(nxt)
                else:
                    return False
                prev = nxt
            
        return True


        

        return True