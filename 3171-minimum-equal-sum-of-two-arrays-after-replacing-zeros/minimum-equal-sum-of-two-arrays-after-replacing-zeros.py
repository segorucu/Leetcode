class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        sm1 = sum(nums1)
        sm2 = sum(nums2)
        one = zeros1 + sm1
        two = zeros2 + sm2
        if zeros1 and zeros2:
            return max(one,two)

        if zeros1 == 0 and zeros2 == 0:
            return sm1 if sm1 == sm2 else -1

        if zeros1 == 0:
            if sm1 < sm2 + zeros2:
                return -1
            else:
                return sm1



        if zeros2 == 0:
            if sm2 < sm1 + zeros1:
                return -1
            else:
                return sm2

            