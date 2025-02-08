from heapq import heapify, heappop, heappush
class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        
        sm = 0
        cnt = 0
        hp = []
        for num in nums:
            if num < 0:
                heappush(hp,num)

            sm += num
            while sm < 0:
                val = heappop(hp)
                sm -= val
                cnt += 1
        

        return cnt
