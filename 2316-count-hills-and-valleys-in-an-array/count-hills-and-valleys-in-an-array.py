class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        

        count = 0
        increasing = 0
        for l,r in pairwise(nums):
            if r > l:
                if increasing == -1:
                    count += 1
                increasing = 1
            if r < l:
                if increasing == 1:
                    count += 1
                increasing = -1

        return count