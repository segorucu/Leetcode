class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        

        def dummy(x):
            return x % 3 != 0
        

        return len(list(filter(lambda x: x%3 != 0,nums)))
        