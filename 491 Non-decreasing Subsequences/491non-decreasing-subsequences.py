class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = set()
        def backtrack(start,curr):
                            
            if len(curr) >= 2:
                tup = tuple(curr[:])
                if tup not in ans: 
                    ans.add(tup)

            if len(curr) == len(nums):
                return

            for i in range(start,n):
                num = nums[i]
                if curr and num < curr[-1]:
                    continue
                curr.append(num)
                backtrack(i+1,curr)
                curr.pop()




        backtrack(0,[])
        return ans