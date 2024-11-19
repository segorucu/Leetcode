class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        counter = collections.defaultdict(int)
        currsm = 0
        ans = 0
        for i, num in enumerate(nums):
            counter[num] += 1
            currsm += num
            if i >= k:
                tmp = nums[i-k]
                currsm -= tmp
                counter[tmp] -= 1
                if counter[tmp] == 0:
                    del counter[tmp]
            if i >= k-1:
                if len(counter) == k:
                    ans = max(ans, currsm)

        return ans



        return 0
