class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1.sort()
        nums2.sort()
        
        n = len(nums1)
        m = len(nums2)
        
        minx = inf
        
        for i in range(n):
            for j in range(i+1,n):
                newarr = nums1[0:i] + nums1[i+1:j] + nums1[j+1:]
                success = True
                if m > 1:
                    for a1, a2, b1, b2 in zip(newarr[0:-1],newarr[1:],nums2[0:-1],nums2[1:]):
                        if a2 - a1 != b2 - b1:
                            success = False
                            break
                    if success:
                        minx = min(minx, b1 - a1)
                else:
                    b1 = nums2[0]
                    a1 = newarr[0]
                    minx = min(minx, b1 - a1)
                    
                         
        return minx
        
        
        
        
            
        
            
            
        