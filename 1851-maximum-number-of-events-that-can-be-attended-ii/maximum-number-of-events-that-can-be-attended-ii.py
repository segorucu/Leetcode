class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort()
        n = len(events)

        @cache
        def dp(k, j):
            if k == 0:
                return 0
            if j == n:
                return 0

            start, end, reward = events[j]
            one = dp(k, j+1)
            while j < n and events[j][0] <= end:
                j += 1
            two = dp(k-1, j) + reward
            return max(one, two)
            

        return dp(k, 0)