from sortedcontainers import SortedList
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:

        seen = SortedList()
        n = len(nums1)
        tot = 0
        for i in range(n):
            num = nums1[i] - nums2[i]
            ind = seen.bisect_left(1-num)
            tot += (len(seen) - ind)
            # print("ind",ind,"num",num)
            seen.add(num)
            # print("num",seen)

    
        return tot
        