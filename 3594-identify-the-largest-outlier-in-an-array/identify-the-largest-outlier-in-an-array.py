class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
        sm = sum(nums)
        # nums.sort(reverse = True)
        counter = Counter(nums)

        maxval = -2000
        for num in nums:
            currsum = sm - num
            if currsum % 2 == 0:
                sumoftheremainder = currsum // 2
                if sumoftheremainder in counter:
                    if sumoftheremainder == num:
                        if counter[num] >= 2:
                            maxval = max(maxval, num)
                    elif counter[num] >= 1:
                        maxval = max(maxval, num)

        return maxval
