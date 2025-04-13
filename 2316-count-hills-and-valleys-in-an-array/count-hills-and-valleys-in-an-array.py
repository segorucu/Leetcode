class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        

        hill = 0
        valley = 0
        increasing = 0
        for l,r in pairwise(nums):
            if r > l:
                if increasing == -1:
                    valley += 1
                increasing = 1
            if r < l:
                if increasing == 1:
                    hill += 1
                increasing = -1

        return valley + hill