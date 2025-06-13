class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
        n = len(nums)

        def go(mid):
            ret = 0
            l = 0
            while l < n-1:
                if nums[l+1] - nums[l] <= mid:
                    ret += 1
                    l += 2
                else:
                    l += 1
            return ret >= p

        left = 0
        right = nums[-1] - nums[0]
        ret = -1
        while left <= right:
            mid = (left + right) // 2
            if go(mid):
                ret = mid
                right = mid - 1
            else:
                left = mid + 1

        return ret