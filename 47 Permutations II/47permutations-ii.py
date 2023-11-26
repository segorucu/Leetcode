class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        array = list(range(n))

        ans = []
        def backtrack(ind,curr):
            if len(curr) == n:
                if curr not in ans:
                    ans.append(curr[:])
                return

            for i in range(0,n):
                if i not in ind:
                    curr.append(nums[i])
                    ind.append(i)
                    backtrack(ind,curr)
                    curr.pop()
                    ind.pop()

        backtrack([],[])

        return ans
        