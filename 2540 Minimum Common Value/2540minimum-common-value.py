class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1 = set(nums1)
        nums2 = set(nums2)

        minval = inf
        for num in nums2:
            if num in nums1 and num < minval:
                minval = num

        if minval == inf:
            return -1
        return minval