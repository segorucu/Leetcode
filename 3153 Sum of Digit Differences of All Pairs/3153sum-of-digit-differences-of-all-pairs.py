class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        
        
        m = len(str(nums[0]))
        n = len(nums)
        ans = 0
        for _ in range(m):
            counter = collections.defaultdict(int)
            for i in range(n):
                curr = nums[i] % 10
                ans += (i-counter[curr])
                counter[curr] += 1
                nums[i] = nums[i] // 10
        
                
        return ans