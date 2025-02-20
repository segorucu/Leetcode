class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        nums = set(nums)

        def backtrack(num):
            if len(num) == n:
                num = "".join(num)
                if num in nums:
                    return None
                else:
                    return num

            num.append("0")
            res = backtrack(num)
            num.pop()
            if res is not None:
                return res
            num.append("1")
            res = backtrack(num)
            num.pop()
            if res is not None:
                return res

        res = backtrack([])
        return res