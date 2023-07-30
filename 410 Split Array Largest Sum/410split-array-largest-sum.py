class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)

        def check(maxsum):
            tot = 0
            sm = 0
            for num in nums:
                if sm + num <= maxsum:
                    sm += num
                else:
                    tot += 1
                    sm = num
            return tot + 1 <= k

        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1


        return ans
