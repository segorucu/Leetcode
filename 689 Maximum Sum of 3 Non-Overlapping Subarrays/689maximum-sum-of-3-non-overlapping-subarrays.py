class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)

        n = len(prefix)
        dp = [n * [(0, 0)] for _ in range(3)]
        for count in range(3):
            prevmax = 0
            for i in range((count+1)*k,n):
                diff = prefix[i] - prefix[i-k]
                if count > 0:
                    diff += dp[count-1][i-k][1]
                if diff > prevmax:
                    prevmax = diff
                    dp[count][i] = (i-k, prevmax)
                else:
                    dp[count][i] = dp[count][i-1]

        ans = 3*[0]
        ans[2] = dp[2][-1][0]
        ans[1] = dp[1][ans[2]][0]
        ans[0] = dp[0][ans[1]][0]
        return ans
            
        