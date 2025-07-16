class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        

        """
        odd + odd = even
        even + even = even
        odd + even = odd
        even + odd = odd
        """

        # option 1 and 2
        n = len(nums)
        odds = 0
        for num in nums:
            if num % 2:
                odds += 1
        evens = n - odds
        ans = max(odds, evens)

        odd = (nums[0] % 2 == 0)
        curr = 1
        for i in range(1,n):
            if odd and nums[i] % 2:
                curr += 1
                odd = False
            elif not odd and nums[i] % 2 == 0:
                curr += 1
                odd = True

        ans = max(ans, curr)
        return ans


