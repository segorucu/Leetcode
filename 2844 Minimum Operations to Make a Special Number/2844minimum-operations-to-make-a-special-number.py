from functools import cache
class Solution:

    def minimumOperations(self, num: str) -> int:
        
        n = len(num)
        if n == 1:
            if num[0] == "0":
                return 0
            else:
                return 1
        first = 0
        zeros = 0
        i = n-1
        while i >= 0 and zeros < 2:
            if num[i] != "0":
                first += 1
            else:
                zeros += 1
            i -= 1
        # if zeros < 2:
        #     first = n

        two = five = False
        zeros = 0
        second = 0
        i = n-1
        while i >= 0 and ((not five) or  (not two)):
            if five and num[i] == "2":
                two = True
            elif not five and num[i] == "5":
                five = True
            else:
                second += 1
            i -= 1
        if not five or not two:
            second = n

        zero = five = False
        zeros = 0
        third = 0
        i = n-1
        while i >= 0 and ((not five) or  (not zero)):
            if zero and num[i] == "5":
                five = True
            elif not zero and num[i] == "0":
                zero = True
            else:
                third += 1
            i -= 1
        if not zero or not five:
            third = n

        seven = five = False
        zeros = 0
        fourth = 0
        i = n-1
        while i >= 0 and ((not five) or  (not seven)):
            if five and num[i] == "7":
                seven = True
            elif not five and num[i] == "5":
                five = True
            else:
                fourth += 1
            i -= 1
        if not seven or not five:
            fourth = n


               

        return min(first,second,third,fourth)