class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        MOD = 10**9+7

        n = len(nums)
        l = 0
        r = n-1
        ans = 0
        while l <= r:
            while l <= r and nums[l] + nums[r] > target:
                r -= 1
                if r < l:
                    break
            if r < l:
                break
            size = r-l
            ans += pow(2,size,MOD)
            ans = ans % MOD
            l += 1

        return ans

            



        # 1
        # 5
        # 10
        # 10
        # 5
        # 1

        # 1
        # 4
        # 6
        # 4
        # 1

        # 1
        # 3
        # 3
        # 1

        # 1
        # 2
        # 1

        # 1
        