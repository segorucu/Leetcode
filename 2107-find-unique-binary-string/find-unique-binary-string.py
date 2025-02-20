class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        nums = set(nums)

        def backtrack(num):
            if len(num) == n:
                if num in nums:
                    return None
                else:
                    return num

            res = backtrack(num+"0")
            if res is not None:
                return res
            res = backtrack(num+"1")
            if res is not None:
                return res

        res = backtrack("")
        return res