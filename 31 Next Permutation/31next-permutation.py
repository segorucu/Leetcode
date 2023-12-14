class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        n = len(nums)

        def reverse(arr,i):
            m = len(arr)
            left = i
            right = m-1
            while left < right:
                arr[right], arr[left] = arr[left], arr[right]
                left += 1
                right -= 1
            return 

        ii = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                for j in range(i+1,n):
                    if nums[j] > nums[i]:
                        k = j
                nums[k], nums[i] = nums[i], nums[k]
                reverse(nums,i+1)
                return nums
        else:
            reverse(nums,0)

        return nums



            
        