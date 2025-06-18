class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n % 3 != 0:
            return []
        ROWS = n // 3

        nums.sort()
        prev = nums[0]
        ans = [[] for _ in range(ROWS)]
        row = 0
        for i, num in enumerate(nums):
            row = i // 3
            if i > 0 and ans[row] and num - min(ans[row]) > k:
                return []
            ans[row].append(num)

        return ans