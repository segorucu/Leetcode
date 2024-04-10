class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()
        n = len(deck)
        queue = collections.deque()
        queue.extend(list(range(n)))
        ans = n * [0]
        i = 0
        while len(queue) >= 2:
            one = queue.popleft()
            two = queue.popleft()
            ans[one] = deck[i]
            queue.append(two)
            i += 1
        if queue:
            one = queue.popleft()
            ans[one] = deck[i]

        return ans
