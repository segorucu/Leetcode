class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        sm = sum(nums)
        if sm % 2:
            return False
        goal = sm // 2
        
        @cache
        def dp(i, sm):
            if i == len(nums):
                if sm == goal:
                    return True
                return False

            return dp(i+1, sm +nums[i]) or dp(i+1, sm)


        return dp(0,0)