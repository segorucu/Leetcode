from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        def reverse(num):
            rev = 0
            while num > 0:
                rev = rev*10 + num % 10
                num = num // 10
            return rev

        freq = defaultdict(int)
        for num in nums:
            freq[num-reverse(num)] += 1
        
        sm = 0
        for values in freq.values():
            sm += values * (values-1) // 2
        return sm % (10**9+7)

                
        
