class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        once = set()
        for num in nums:
            if num in once:
                once.remove(num)
            else:
                once.add(num)

        return once