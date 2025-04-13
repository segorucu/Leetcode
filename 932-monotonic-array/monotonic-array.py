class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        i = 0
        n = len(nums)
        decreasing = False
        increasing = False
        while i < n-1:
            if nums[i] == nums[i+1]:
                while i < n-1 and nums[i] == nums[i+1]:
                    i += 1
            elif nums[i] < nums[i+1]:
                if decreasing:
                    return False
                increasing = True
                i += 1
            else:
                if increasing:
                    return False
                decreasing = True
                i += 1
        return True
            
            

        return False