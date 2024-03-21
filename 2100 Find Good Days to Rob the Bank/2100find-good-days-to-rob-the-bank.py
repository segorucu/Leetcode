class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:

        n= len(security)
        decreasing = n * [0]
        for i in range(1,n):
            if security[i] <= security[i-1]:
                decreasing[i] = decreasing[i-1] + 1

        increasing = n * [0]
        for i in range(n-2,-1,-1):
            if security[i] <= security[i+1]:
                increasing[i] = increasing[i+1] + 1

        # print(decreasing, increasing)
        ans = []
        for i in range(time,n-time):
            if decreasing[i] >= time and increasing[i] >= time:
                ans.append(i)

        return ans
            

        