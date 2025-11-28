class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
    

        return sum(map(lambda x: 0 if x%3 == 0 else 1,nums))
        