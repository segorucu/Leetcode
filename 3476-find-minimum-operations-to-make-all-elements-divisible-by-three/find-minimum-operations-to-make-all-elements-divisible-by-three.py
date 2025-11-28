class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
    

        return sum(map(lambda x: x%3 != 0,nums))
        