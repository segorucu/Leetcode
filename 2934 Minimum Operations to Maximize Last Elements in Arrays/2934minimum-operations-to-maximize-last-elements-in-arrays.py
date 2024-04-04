class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        
        end1 = nums1[-1]
        end2 = nums2[-1]

        if end1 > end2:
            large = end1
            small = end2
            largearr = nums1[:-1].copy()
            smallarr = nums2[:-1].copy()
        else:
            large = end2
            small = end1
            largearr = nums2[:-1].copy()
            smallarr = nums1[:-1].copy()
            

        # option1 - collect the bigger ones in nums2
        count1 = 0
        count2 = 1
        for sm, lr in zip(smallarr, largearr):
            if max(sm,lr) > large:
                return -1
            if min(sm,lr) > small:
                return -1
            if sm > small:
                count1 += 1
            if lr > small:
                count2 += 1

        return min(count1,count2)



        
        