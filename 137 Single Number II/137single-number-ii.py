from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counter = defaultdict(int)
        counter2 = defaultdict(int)
        pos = 0 
        mask = 1
        for bit in range(32):
            for num in nums:
                if abs(num) & mask:
                    if num > 0:
                        counter[bit] += 1
                        counter[bit] %= 3
                    elif num < 0:
                        counter2[bit] += 1
                        counter2[bit] %= 3

            mask = mask << 1

       
        mask = 1
        sm = 0
        sm2 = 0
        for bit in range(32):
            if counter[bit]:
                sm += mask * counter[bit]
            if counter2[bit]:
                sm2 -= mask * counter2[bit]
            mask = mask << 1
        return sm + sm2