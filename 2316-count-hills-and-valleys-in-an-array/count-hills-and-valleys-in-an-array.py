class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        

        hill = 0
        valley = 0
        decreasing = False
        increasing = False
        for l,r in pairwise(nums):
            if r > l:
                if decreasing:
                    valley += 1
                    # print(l,r)
                increasing = True
                decreasing = False
            if r < l:
                if increasing:
                    hill += 1
                    # print(l,r)
                decreasing = True
                increasing = False

        return valley + hill