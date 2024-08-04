class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        MOD = 10**9+7
        arr = []
        n = len(nums)
        for i in range(n):
            curr = 0
            for j in range(i,n):
                curr += nums[j]
                arr.append(curr)

        arr.sort()
        ans = sum(arr[left-1:right])
        # print(arr)
        return ans % MOD