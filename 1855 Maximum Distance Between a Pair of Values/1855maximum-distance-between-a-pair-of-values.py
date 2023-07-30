class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        ans = 0
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            left = i
            right = m - 1
            dum = -1
            while left <= right:
                mid = (left + right) // 2
                if nums1[i] > nums2[mid]:
                    right = mid - 1
                else:
                    dum = mid
                    left = mid + 1
            ans = max(ans,dum-i)
        return ans