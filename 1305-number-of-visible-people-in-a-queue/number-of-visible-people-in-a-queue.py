class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        count = n * [0]
        hp = []
        for i,h in enumerate(heights):
            while hp and hp[0][0] <= h:
                _, ind = heappop(hp)
                count[ind] += 1
            if hp:
                count[hp[0][1]] += 1
            heappush(hp,(h,i))

        return count
