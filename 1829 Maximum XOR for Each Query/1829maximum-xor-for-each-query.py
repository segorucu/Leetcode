class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        

        maxval = 2 ** maximumBit - 1
        curr = 0
        ans = []
        for num in nums:
            curr = curr ^ num
            val = curr ^ maxval
            ans.append(val)

        return list(reversed(ans))