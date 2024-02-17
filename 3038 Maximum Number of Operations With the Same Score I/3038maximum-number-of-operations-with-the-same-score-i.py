class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 1
        n = len(nums)
        prev = nums[0] + nums[1]
        ops = 0
        while fast < n:
            new = nums[slow] + nums[fast]
            if new != prev:
                break
            else:
                ops += 1
                slow += 2
                fast += 2
                
        return ops
                
            