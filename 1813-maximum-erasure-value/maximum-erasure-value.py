class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        l = 0
        n = len(nums)
        ans = 0
        sm = 0
        counter = defaultdict(int)
        for r in range(n):
            sm += nums[r]
            counter[nums[r]] += 1
            while counter[nums[r]] > 1:
                counter[nums[l]] -= 1
                sm -= nums[l]
                l += 1
            ans = max(ans, sm)




        return ans