class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        

        minsm = 0
        curr = 0
        for num in differences:
            curr += num
            minsm = min(minsm, curr)

        n = len(differences)
        ans = (n+1) * [0]
        ans[0] = lower + abs(minsm)

        for i,diff in enumerate(differences):
            ans[i+1] = ans[i] + diff

        maxval = max(ans)

        return max(0,upper - maxval + 1)