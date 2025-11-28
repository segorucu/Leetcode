class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        

        def dummy(x):
            if x % 3 == 0:
                return 0
            else:
                return 1

        return sum(map(dummy,nums))
        