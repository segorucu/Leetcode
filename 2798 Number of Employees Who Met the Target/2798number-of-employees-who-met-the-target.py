class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        tot = 0
        for hour in hours:
            if hour >= target:
                tot += 1
                
        return tot
        