from collections import defaultdict
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        

        access_times = sorted(access_times)
        employee_times = defaultdict(list)
        for employee, time in access_times:
            employee_times[employee].append(time)
            
        ans = []
        for employee, times in employee_times.items():
            if len(times) < 3:
                continue
            data = []
            for time in times:
                hour = int(time[0:2])
                minutes = int(time[2:4])
                total = hour * 60 + minutes
                data.append(total)
            n = len(data)
            for i in range(2,n):
                if data[i] - data[i-2] < 60:
                    ans.append(employee)
                    break
                    
        return ans
                
            
        