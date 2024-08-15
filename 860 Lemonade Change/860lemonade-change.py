class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        holding = {5:0, 10:0, 20:0}

        for i, bill in enumerate(bills):
            if bill == 10:
                if holding[5] > 0:
                    holding[5] -= 1
                elif holding[5] == 0:
                    return False
            elif bill == 20:
                if holding[10] > 0 and holding[5] > 0:
                    holding[10] -= 1
                    holding[5] -= 1
                elif holding[5] >= 3:
                    holding[5] -= 3
                else:
                    return False
            holding[bill] += 1

        return True

