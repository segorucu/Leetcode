class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        if not nums:
            return [[lower,upper]]

        ans = []
        if lower < nums[0]:
            ans.append([lower,nums[0]-1])

        expected = nums[0] + 1
        for i, num in enumerate(nums[1:]):
            # print(num, expected)
            if num != expected:
                ans.append([expected,num-1])
                expected = num + 1
            else:
                expected += 1

        if upper > nums[-1]:
            ans.append([nums[-1]+1,upper])

        return ans

