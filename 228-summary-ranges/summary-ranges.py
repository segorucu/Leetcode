class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        nums.append(2**33)
        ans = []
        n = len(nums)
        begin = 0
        for i in range(1,n):
            if nums[i] > nums[i-1] + 1:
                if begin == i-1:
                    ans.append(str(nums[begin]))
                else:
                    ans.append(str(nums[begin])+"->"+str(nums[i-1]))
                begin = i

        return ans

