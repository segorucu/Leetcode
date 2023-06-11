class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        sm = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            sm.append(sm[i-1]+nums[i])
            
        return sm
        