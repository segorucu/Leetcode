from heapq import heapify, heappop, heappush
class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        marked = set()
        n = len(nums)
        hp = []
        for i,num in enumerate(nums):
            heappush(hp,(num,i))

        score = 0
        while hp:
            val, i = heappop(hp)
            if i not in marked:
                marked.add(i)
                marked.add(i+1)
                marked.add(i-1)
                score += val

        return score

        

