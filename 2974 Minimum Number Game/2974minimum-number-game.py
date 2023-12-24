class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        temp = []
        
        while nums:
            temp = []
            for i in range(2):
                minval = min(nums)
                nums.remove(minval)
                temp.append(minval)
            temp.reverse()
            arr.extend(temp)

        return arr
 