class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        

        def del1(digits):
            if len(digits) == 0:
                return []
            ones = [1,4,7]
            for one in ones:
                if one in digits:
                    digits.remove(one)
                    return digits
            return del2(del2(digits))

        def del2(digits):
            if len(digits) == 0:
                return [] 
            twos = [2,5,8]
            for two in twos:
                if two in digits:
                    digits.remove(two)
                    return digits
            return del1(del1(digits))

        digits.sort()
        sm = sum(digits)
        if sm == 0:
            return "0"

        elif sm % 3 == 1:
            digits = del1(digits)
        elif sm % 3 == 2:
            digits = del2(digits)
        digits = digits[::-1]

        if sum(digits) == 0:
            if 0 not in digits:
                return ""
            return "0"
        return "".join([str(a) for a in digits])            
        
