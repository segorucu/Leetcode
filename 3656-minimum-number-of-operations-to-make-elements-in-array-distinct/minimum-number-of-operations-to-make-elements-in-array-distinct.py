class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        

        n = len(nums)
        visited = set()
        for i in range(n-1,-1,-1):
            if nums[i] not in visited:
                visited.add(nums[i])
            else:
                break
        else:
            return 0

        keep = len(nums[i+1:])
        # print(n-keep)
        return (n-keep-1)//3+1

