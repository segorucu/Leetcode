class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        sm = sum(nums)
        curr = 0
        ans = 0
        for i, num in enumerate(nums):
            curr += num
            if num == 0:
                if sm % 2:
                    if curr == sm // 2 or curr == (sm+1) // 2:
                        ans += 1
                else:
                    if curr == sm // 2:
                        ans += 2

        return ans
                


        