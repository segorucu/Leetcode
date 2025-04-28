class Solution:
    def countSubarrays(self, nums, k):

        count = 0
        l = r = 0
        n = len(nums)
        sm = 0
        ln = 0
        for r in range(n):
            sm += nums[r]
            ln = r-l+1
            while sm*ln >= k:
                sm -= nums[l]
                l += 1
                ln = r-l+1

            count += r-l+1

        return count
