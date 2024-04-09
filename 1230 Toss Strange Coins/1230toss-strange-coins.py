from functools import cache
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        n = len(prob)
        @cache
        def dp(i,target):
            if i == n:
                if target == 0:
                    return 1
                else:
                    return 0

            head = 0
            if target > 0:
                head = dp(i+1,target-1)
            tail = dp(i+1,target)
            return head*prob[i] + tail*(1-prob[i])
        return dp(0,target)