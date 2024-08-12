class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        
        one = 0
        for val in arr1:
            one = one ^ val
        two = 0
        for val in arr2:
            two = two ^ val
        ans = one & two
        return ans