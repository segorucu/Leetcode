class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        

        arr = SortedList()
        for num in nums:
            arr.add(num)

        n = len(nums)
        ans = n * [0]

        for i,num in enumerate(nums):
            
            ind = bisect_left(arr,num)
            ans[i] = ind
            arr.remove(num)


        return ans