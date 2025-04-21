class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        

        minsm = 0
        maxsm = 0
        maxsm = 0
        curr = 0
        for num in differences:
            curr += num
            minsm = min(minsm, curr)
            maxsm = max(maxsm, curr)

        return max(0,upper - lower - maxsm + minsm + 1)