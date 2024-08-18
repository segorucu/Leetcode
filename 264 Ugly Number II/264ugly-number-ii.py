class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        nums = [1]
        i2 = i3 = i5 = 0
        for _ in range(n):
            curr = min(2*nums[i2], 3*nums[i3], 5*nums[i5])

            if curr == 2*nums[i2]:
                i2 += 1
            if curr == 3*nums[i3]:
                i3 += 1
            if curr == 5*nums[i5]:
                i5 += 1
            nums.append(curr)
        
        # print(nums)
        return nums[n-1]
            
