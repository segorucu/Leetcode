class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        

        def ispalindrome(arr):
            left = 0
            right = len(arr)-1
            while left < right:
                if arr[left] != arr[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def numtolist(num):
            arr = []
            while num > 0:
                rem = num % 10
                num = num // 10
                arr.append(rem)
            return arr
        
        def calccost(arr,val):
            cost = 0
            for a in arr:
                cost += abs(a-val)
            return cost
        
        if n == 1:
            num = nums[0]
            arr = numtolist(num)
            if ispalindrome(arr) == False:
                for diff in range(1,10000):
                    num = nums[0] + diff
                    arr = numtolist(num)
                    if ispalindrome(arr):
                        return num - nums[0]
                    num = nums[0] - diff
                    arr = numtolist(num)
                    if ispalindrome(arr):
                        return nums[0] - num
            else:
                return 0
            
        

        if n % 2 == 1:
            mid = n // 2
            midval = nums[mid]
        elif n % 2 == 0:
            mid = n // 2
            midval = (nums[mid] + nums[mid-1]) // 2
        arr = numtolist(midval)
        if ispalindrome(arr) == True:
            return calccost(nums,midval)

        num = midval
        while True:
            num += 1
            arr = numtolist(num)
            if ispalindrome(arr) == True:
                right = calccost(nums,num)
                break

        num = midval
        while True:
            num -= 1
            arr = numtolist(num)
            if ispalindrome(arr) == True:
                left = calccost(nums,num)
                break


        return min(left,right)

