class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def rob1(arr):

            n = len(arr)
            dp = (n+1) * [0]
            dp[1] = arr[0]
            for i in range(1,n):
                dp[i+1] = max(dp[i],dp[i-1]+arr[i])

            return dp[-1]

        one = rob1(nums[0:-1])
        two = rob1(nums[1:])


        return max(one,two)