class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        n = len(nums)
        smallest = n * [0]
        minval = inf
        for i in range(n-1,-1,-1):
            smallest[i] = minval
            minval = min(minval,nums[i])

        largest = n * [0]
        maxval = -1
        for i in range(n):
            maxval = max(maxval,nums[i])
            largest[i] = maxval

        for i in range(n):
            if largest[i] <= smallest[i]:
                return i + 1

        print(smallest)

        return 0