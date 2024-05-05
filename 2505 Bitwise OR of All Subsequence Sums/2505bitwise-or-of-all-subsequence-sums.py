class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        
        counter = 64 * [0]
        for num in nums:
            for index in range(32):
                mask = 1 << index
                if num & mask == mask:
                    counter[index] += 1

        ans = 0
        for i in range(63):
            if counter[i] > 0:
                ans |= (1 << i)
            counter[i+1] += counter[i] // 2

        return ans