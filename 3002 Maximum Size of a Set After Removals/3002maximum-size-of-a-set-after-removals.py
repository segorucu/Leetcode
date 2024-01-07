class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        
        intersection = set(nums1) & set(nums2)
        nums1o = set()
        for num in nums1:
            if num not in intersection:
                nums1o.add(num)
        nums2o = set()
        for num in nums2:
            if num not in intersection:
                nums2o.add(num)
                
        n = len(nums1)
        half = n // 2
        ans = 0
        if len(nums1o) > half:
            ans += 1
        
        
        # print(min(len(nums1o),half),min(len(nums2o),half))
        return min(min(len(nums1o),half) + min(len(nums2o),half) + len(intersection),n)
        
        
        