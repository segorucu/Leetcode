class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        
        nums.sort()
        n = len(nums)
        if n == 1:
            return nums
        
        mp = collections.defaultdict(list)
        dp = n * [1]

        mp[0] = [nums[0]]
        maxval = 0
        ind = 0
        for i in range(1,n):
            mp[i] = [nums[i]]
            for j in range(0,i):
                if nums[i] % nums[j] == 0 and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
                    mp[i] = mp[j] + [nums[i]]
                    if dp[i] > maxval:
                        maxval = dp[i]
                        ind = i


        return mp[ind]



        