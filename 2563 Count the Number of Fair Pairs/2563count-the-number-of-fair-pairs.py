from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        '''
        # lower <= num+x <= upper
        lower - num <= x <= upper - num


        '''


        nums.sort()
        count = 0
        prefix = []
        for i, num in enumerate(nums):
            lowergoal = lower - num
            uppergoal = upper - num
            lowerindex = bisect_left(prefix, lowergoal)
            upperindex = bisect_right(prefix, uppergoal)
            # if upperindex > lowerindex and upperindex < len(prefix):
            count += upperindex - lowerindex
            # print(prefix, upperindex, lowerindex, count)
            prefix.append(num)

        return count
            