class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        once = set()
        deleted = set()
        
        for num in nums:
            if num in once:
                once.remove(num)
                deleted.add(num)
            elif num not in deleted:
                once.add(num)
            
        if len(once) == 0:
            return -1
        else:
            return max(once)
                
        