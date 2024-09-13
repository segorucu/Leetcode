class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        changes = (k+2) * [0]
        changes[0] = n //2
        l = 0
        r = n-1
        while l < r:
            left = nums[l]
            right = nums[r]
            curr_diff = abs(left-right)
            max_diff = max(left, right, k-left, k-right)
            changes[curr_diff] -= 1
            changes[curr_diff+1] += 1
            changes[max_diff+1] += 1
            l, r = l+1, r-1

        for i in range(1,len(changes)):
            changes[i] += changes[i-1]

        return min(changes)
