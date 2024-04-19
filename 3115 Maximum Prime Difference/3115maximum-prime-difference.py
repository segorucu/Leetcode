class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:

        def is_prime(n):
            if n < 2:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        seen = set()
        primeset = set()
        ans = []
        for i, num in enumerate(nums):
            if num in seen:
                if num in primeset:
                    ans.append(i)
            else:
                if is_prime(num):
                    primeset.add(num)
                    ans.append(i)
                seen.add(num)

        return ans[-1] - ans[0]
        