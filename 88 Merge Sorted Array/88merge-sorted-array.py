class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        fin = nums1[0:m]+nums2[0:n]
        #print(fin)
        fin = sorted(fin)
        for i, val in enumerate(fin):
            nums1[i] = val

        