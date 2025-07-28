class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        target = 0
        for num in nums:
            target |= num

        currarr = []
        def backtrack(i, ORval):
            if i == len(nums):
                if not currarr or ORval != target:
                    return 0
                else:
                    return 1
        
            currarr.append(i)
            ret = backtrack(i+1, ORval | nums[i])
            currarr.pop()
            ret += backtrack(i+1, ORval)
            return ret

        return backtrack(0, 0)

