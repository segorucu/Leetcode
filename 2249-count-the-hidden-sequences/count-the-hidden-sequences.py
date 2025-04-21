class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        

        minsm = 0
        curr = 0
        for num in differences:
            curr += num
            minsm = min(minsm, curr)

        curr = lower + abs(minsm)
        maxval = curr
        for i,diff in enumerate(differences):
            curr += diff
            maxval = max(maxval, curr)

        return max(0,upper - maxval + 1)