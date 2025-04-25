class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        
        for i,num in enumerate(nums):
            nums[i] = 1 if nums[i] % modulo == k else 0

        prefix = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            prefix.append(prefix[-1] + nums[i])

        # print(prefix)

        counter = defaultdict(int)
        counter[0] = 1
        ans = 0
        for num in prefix: 
            ans += counter[(num-k) % modulo]
            counter[num%modulo] += 1

        return ans

        # prefix = [1,1,2,3]
        # counter = [0:2, 1:2, 2:0]
        # ans = 2
        # num = 3
        # curr = 0