class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned = set(banned)
        sm = 0
        count = 0
        for i in range(1,n+1):
            if i in banned:
                continue
            cand = sm + i
            if cand <= maxSum:
                count += 1
                sm = cand
            else:
                break
        return count