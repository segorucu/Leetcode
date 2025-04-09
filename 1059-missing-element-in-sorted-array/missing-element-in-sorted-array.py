class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        

        minval = nums[0]
        maxval = 10**9

        left = minval
        right = maxval


        def go(mid):
            ind = bisect_right(nums,mid)
            # if ind < len(nums) and mid == nums[ind]:
            #     ind += 1
            return mid >= minval + ind + k -1

        res = 0
        while left <= right:
            mid = (left+right) // 2
            if go(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res