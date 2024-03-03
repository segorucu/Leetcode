class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2,n):
            num = nums[i]
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
                
            
        return arr1+arr2
        