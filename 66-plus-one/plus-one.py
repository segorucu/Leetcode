class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        
        n = len(digits)
        p = n-1
        carry = 1
        while p >= 0:
            if digits[p] < 9:
                digits[p] += carry
                return digits
            else:
                digits[p] = 0
                carry = 1
            p -=1
        else:
            if carry == 1:
                return [1] + digits

        return digits