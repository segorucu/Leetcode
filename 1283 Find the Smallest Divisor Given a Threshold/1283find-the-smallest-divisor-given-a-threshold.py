class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def check(divisor):
            tot = 0
            for num in nums:
                tot += math.ceil(num/divisor)
            return tot <= threshold

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left