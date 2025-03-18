class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        # counter = collections.defaultdict(list)

        # for i,num  in enumerate(nums):
        #     for digit in range(30):
        #         mask = 1 << digit
        #         if (num & mask):
        #             counter[i].append(digit)
    
        maxdigit = 30
        n = len(nums)
        currmp = collections.defaultdict(int)


        def check(num):
            for digit in range(maxdigit):
                mask = 1 << digit
                if (num & mask) and currmp[digit] > 0:
                    return True
            return False

        def moveright(num):
            for digit in range(maxdigit):
                mask = 1 << digit
                if (num & mask):
                    currmp[digit] -= 1

        def addright(num):
            for digit in range(maxdigit):
                mask = 1 << digit
                if num & mask:
                    currmp[digit] += 1

        ans = 0
        l = 0
        for r in range(n):
            while check(nums[r]):
                moveright(nums[l])
                l += 1
            addright(nums[r])
            ans = max(ans, r-l+1)

        
        return ans
