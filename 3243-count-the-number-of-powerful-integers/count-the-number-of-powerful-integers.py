class Solution:
    def calculate(self, finish_, limit, s):
        if len(finish_) < len(s):
            return 0
        elif len(finish_) == len(s):
            if finish_ < s:
                return 0
            else:
                return 1

        
        pre_len = len(finish_) - len(s)
        suffix = finish_[pre_len:]
        count = 0

        for i in range(pre_len):
            if int(finish_[i]) > limit:
                count += (limit + 1) ** (pre_len - i)
                return count
            count += int(finish_[i]) * (limit + 1) ** ( pre_len - i - 1)

        if suffix >= s:
            count += 1

        return count
            


        
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        upper = self.calculate(str(finish), limit, s)
        lower = self.calculate(str(start-1), limit, s)
        return upper - lower
        
        


        
            

        

