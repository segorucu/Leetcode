class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        n = len(nums)
        evens = n * [0]
        odds = n * [0]
        fair = 0

        evens[0] = nums[0]
        for i in range(1,n):
            num = nums[i]
            if i % 2 == 0:
                evens[i] += evens[i-1] + num
                odds[i] = odds[i-1]
            else:
                evens[i] = evens[i-1]
                odds[i] += odds[i-1] + num

        for i in range(n):
            num = nums[i]
            oddsm = 0
            evensm = 0
            if i > 0:
                oddsm += odds[i-1]
                evensm += evens[i-1]
            if i < n-1:
                oddsm += evens[-1]-evens[i]
                evensm += odds[-1]-odds[i]
            if evensm == oddsm:
                fair += 1

        return fair

        