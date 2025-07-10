class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        

        startTime = [0] + startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]

        n = len(startTime)
        stack = []
        max_freetime_hp = []
        for i in range(1,n-1):
            freetime_prev = startTime[i] - endTime[i-1]
            freetime_post = startTime[i+1] - endTime[i]
            duration = endTime[i] - startTime[i]
            stack.append([duration, freetime_prev, freetime_post])
            if len(max_freetime_hp) < 3 or freetime_prev > max_freetime_hp[0]:
                heappush(max_freetime_hp, freetime_prev)
            while len(max_freetime_hp) > 3:
                heappop(max_freetime_hp)
        else:
            if len(max_freetime_hp) < 3 or freetime_post > max_freetime_hp[0]:
                heappush(max_freetime_hp, freetime_post)
            while len(max_freetime_hp) > 3:
                heappop(max_freetime_hp)

        max_freetime_hp.sort()
        ans = max_freetime_hp[-1]
        for duration, prev, post in stack:
            curr = []
            if prev in max_freetime_hp:
                max_freetime_hp.remove(prev)
                curr.append(prev)
            if post in max_freetime_hp:
                max_freetime_hp.remove(post)
                curr.append(post)
            if duration <= max(max_freetime_hp):
                ans = max(ans, duration + prev + post)
            else:
                ans = max(ans, prev + post)
            max_freetime_hp.extend(curr)

        return ans
        
