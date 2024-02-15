class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort(reverse=True)

        n = len(nums)
        prefix = n * [0]
        prefix[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            prefix[i] += prefix[i+1] + nums[i]

        for i in range(n-2):
            if prefix[i] < 2*prefix[i+1]:
                return prefix[i]
        return -1
        