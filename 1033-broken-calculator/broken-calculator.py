class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        curr = startValue
        if curr > target:
            return curr - target

        ops = 0
        while target >= 2 * curr:
            if target % 2:
                target += 1
                ops += 1
            else:
                target = target // 2
                ops += 1

        if target == curr:
            return ops
            
        oldcurr = curr
        #option 1
        op1 = curr - (target+1) // 2
        curr -= op1
        op1 += 1
        curr *= 2
        op1 += curr - target

        curr = oldcurr
        #option 2
        op2 = 1
        curr *= 2
        op2 += curr - target

        add = min(op1,op2)
        return ops + add
        

        

        