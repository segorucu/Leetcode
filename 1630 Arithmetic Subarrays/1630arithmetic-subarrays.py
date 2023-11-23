class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        if len(nums) == 2:
            return m * [True]

        ans = []
        for k in range(m):
            left = l[k]
            right = r[k]
            dums = nums[left:right+1].copy()
            dums = sorted(dums)
            decision = True
            for i in range(len(dums)-1):
                diff = dums[i+1] - dums[i]
                if i > 0 and diff != diff0:
                    decision = False
                    break
                elif i == 0:
                    diff0 = diff
            ans.append(decision)

        return ans
                

                    
                    
