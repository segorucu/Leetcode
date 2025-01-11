class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        tot = m + n
        med = tot // 2

        nums = []
        p1 = p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
        while p1 < m:
            nums.append(nums1[p1])
            p1 += 1
        while p2 < n:
            nums.append(nums2[p2])
            p2 += 1

        if tot % 2 == 1:
            return nums[med]
        else:
            return (nums[med-1]+nums[med])/2