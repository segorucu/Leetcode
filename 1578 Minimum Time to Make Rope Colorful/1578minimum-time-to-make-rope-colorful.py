class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        n = len(colors)
        def findunion(left):
            right = left
            while right < n-1 and colors[right] == colors[right+1]:
                right += 1
            cost = 0
            if right > left:
                cost = sum(neededTime[left:right+1]) - max(neededTime[left:right+1])
            return cost, right



        
        ans = 0
        pt = 0
        while pt < n:
            cost,pt = findunion(pt)
            ans += cost
            pt += 1

        return ans
        