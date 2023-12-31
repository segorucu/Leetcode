class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        
        sm = 0
        for num in nums:
            if num % 2 == 0:
                sm += 1
            if sm >= 2:
                return True
            
        return False