class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        stack = []
        for i, num in enumerate(nums):
            stack.append((num,i))

        stack.sort()

        n = len(nums)
        visited = set()
        curr = 0
        currsm = sum(nums)
        ans = []
        for i,k in queries:
            if i not in visited:
                currsm -= nums[i]
                visited.add(i)
            j = 0
            while curr < n and j < k:
                ind = stack[curr][1]
                if ind not in visited:
                    currsm -= stack[curr][0]
                    visited.add(ind)
                    j += 1
                curr += 1
            ans.append(currsm)

        return ans