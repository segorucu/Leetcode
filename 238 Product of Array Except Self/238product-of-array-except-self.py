class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for num in nums:
            if num != 0:
                product *= num
        zeros = nums.count(0)
        if zeros > 1:
            return len(nums) * [0]
        elif zeros == 1:
            arr = len(nums) * [0]
            for i,num in enumerate(nums):
                if num == 0:
                    arr[i] = product
                    return arr

        arr = []
        for num in nums:
            arr.append(product // num)
        return arr
        