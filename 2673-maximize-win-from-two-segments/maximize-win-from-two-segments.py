class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:

        n = len(prizePositions)
        def calculate(k):
            ans = n * [0]
            l = 0
            for r in range(n):
                while prizePositions[l] < prizePositions[r] - k:
                    l += 1
                ans[r] = r - l + 1
            return ans

        minval = max(calculate(2*k))
        small = calculate(k)
        @cache
        def dp(i,remain):
            if i < 0 or remain <= 0:
                return 0

            one = dp(i-small[i],remain-1) + small[i]
            two = dp(i-1,remain)
            # print(i, remain, one, two)
            return max(one, two)

        ans0 = dp(n-1,2)

        return max(minval,ans0)