class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        ans = []
        n = len(nums)

        def backtrack(j,curr):
            if len(curr) > len(nums):
                return

            ans.append(curr[:])
            for i in range(j,n):
                curr.append(nums[i])
                backtrack(i+1,curr)
                curr.pop()

        backtrack(0,[])
        return ans