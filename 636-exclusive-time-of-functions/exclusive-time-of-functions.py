class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        ans = n * [0]
        stack = []
        for timestamp in logs:
            idf, action, time = timestamp.split(":")
            idf = int(idf)
            time = int(time)
            if action == "start":
                if stack:
                    ans[stack[-1]] += time - previous_time
                previous_time = time
                stack.append(idf)
            else:
                ans[stack.pop()] += time - previous_time + 1
                previous_time = time + 1
                
                    
        return ans


        