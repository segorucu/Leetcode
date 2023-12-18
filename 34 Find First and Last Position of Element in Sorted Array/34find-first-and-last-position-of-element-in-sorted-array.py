class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
    
        if n == 0:
            return [-1,-1]
        # if n == 1:
        #     if nums[0] == target:
        #         return [0,0]
        #     else:
        #         return [-1,-1]
        # if n == 2:
        #     if target not in nums:
        #         return [-1,-1]
        #     if nums[0] == target:
        #         left = 0
        #     else:
        #         left = 1
        #     if nums[1] == target:
        #         right = 1
        #     else:
        #         right = 0
        #     return [left,right]

        def helper(left,leftBias):
            right = len(nums) - 1
            i = -1
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    i = mid
                    if leftBias:
                        right = mid - 1
                    else:
                        left=  mid + 1
            return i

        left = helper(0,True)
        right = helper(left,False)
            
        return [left,right]


