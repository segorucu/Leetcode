class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        

        sm = sum(nums)
        if sm % 3 == 0:
            return sm

        nums.sort()
        ones = []
        twos = []
        for num in nums:
            if num % 3 == 1 and len(ones) < 3:
                ones.append(num)
            elif num % 3 == 2 and len(twos) < 3:
                twos.append(num)
        
        if sm % 3 == 1:
            one = sm
            if ones:
                one = min(one, ones[0])
            if len(twos) > 1:
                one = min(one, sum(twos[0:2]))
            return sm - one
        elif sm % 3 == 2:
            two = sm
            if len(ones) > 1:
                two = min(two, sum(ones[0:2]))
            if twos:
                two = min(two, twos[0])
            return sm - two




        

        