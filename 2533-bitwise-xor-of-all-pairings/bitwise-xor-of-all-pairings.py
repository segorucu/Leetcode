class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1 = len(nums1)
        n2 = len(nums2)

        one = 0
        for num in nums1:
            one ^= num

        two = 0
        for num in nums2:
            two ^= num


        if n1 % 2 == 0 and n2 % 2 == 0:
            return 0
        elif n1 % 2 == 1 and n2 % 2 == 0:
            return two
        elif n1 % 2 == 0 and n2 % 2 == 1:
            return one
        else:
            return one ^ two