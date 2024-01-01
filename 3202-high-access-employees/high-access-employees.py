from typing import List

class Solution:
    def time_diff(self, time1, time2):
        return (int(time2[:2]) - int(time1[:2])) * 60 + int(time2[2:]) - int(time1[2:])

    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times.sort() 
        
        result_set = set()  
        
        for i in range(len(access_times) - 2):
            employee_id = access_times[i][0]
            
            if employee_id == access_times[i + 2][0]:
                time_difference2 = self.time_diff(access_times[i][1], access_times[i + 2][1])

                if time_difference2 <= 59:
                    result_set.add(employee_id)

        return list(result_set)
