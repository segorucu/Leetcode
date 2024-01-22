class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        ans = 2 *[0]
        n = len(nums)
        for i in range(1,n+1):
            if counter[i] == 2:
                ans[0] = i
            elif i not in counter:
                ans[1] = i

        return ans
        