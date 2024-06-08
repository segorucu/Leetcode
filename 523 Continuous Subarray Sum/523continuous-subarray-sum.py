class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        visited = set()
        n = len(nums)
        curr = nums[0] % k
        visited.add(0)
        visited.add(curr)

        for i in range(1,n):
            curr += nums[i]
            curr %= k
            if nums[i] % k == 0:
                if nums[i-1] % k == 0:
                    return True
            elif curr in visited:
                return True
            visited.add(curr)
        return False