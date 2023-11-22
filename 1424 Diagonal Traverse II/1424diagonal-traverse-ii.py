class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ni = len(nums)
        lst = []
        for i in range(ni):
            for j, val in enumerate(nums[i]):
                lst.append((i+j,-i,val))

        lst = sorted(lst)
        ans = []
        for (sm, row, val) in lst:
            ans.append(val)

        return ans
        