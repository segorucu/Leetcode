class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort()

        sm = 0
        for day in range(k):
            curr = happiness.pop() - day
            if curr < 0:
                break
            sm += curr


        return sm