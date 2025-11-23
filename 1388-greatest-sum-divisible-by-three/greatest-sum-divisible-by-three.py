class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        nums.sort()
        sm = 0
        n = len(nums)
        ones = []
        twos = []
        for num in nums:
            if num % 3 == 0:
                sm += num
            elif num % 3 == 1:
                ones.append(num)
            elif num % 3 == 2:
                twos.append(num)

        while len(ones) > 3 and len(twos) > 3:
            sm += ones.pop()
            sm += twos.pop()

        while len(ones) > 5:
            sm += ones.pop()
            sm += ones.pop()
            sm += ones.pop()

        while len(twos) > 5:
            sm += twos.pop()
            sm += twos.pop()
            sm += twos.pop()


        remainder = [0]
        arr = ones + twos
        def backtrack(i, currsm):
            if i == len(arr):
                if currsm % 3 == 0:
                    remainder[0] = max(remainder[0], currsm)
                return

            backtrack(i+1, currsm+arr[i])
            backtrack(i+1, currsm)

        
        backtrack(0, 0)

        return sm + remainder[0]

        

        