from collections import deque
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        
        n = len(nums)

        @cache
        def dp(turn,l,r):
            if l == r:
                if turn % 2 == 0:
                    return nums[l]
                else:
                    return 0

            if turn % 2 == 0:
                return max(dp(turn+1,l+1,r) + nums[l], dp(turn+1,l,r-1) + nums[r])
            else:
                return min(dp(turn+1,l+1,r) - nums[l], dp(turn+1,l,r-1) - nums[r])
            

        res = dp(0,0,n-1)
        return res >= 0




        