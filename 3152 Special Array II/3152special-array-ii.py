class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        m = len(queries)
        n = len(nums)

        prefix = [0]
        for i in range(1,n):
            if nums[i] % 2 == nums[i-1] % 2:
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(prefix[-1])

        ans = []
        for beg,end in queries:
            if prefix[end] - prefix[beg] > 0:
                ans.append(False)
            else:
                ans.append(True)

        return ans

        