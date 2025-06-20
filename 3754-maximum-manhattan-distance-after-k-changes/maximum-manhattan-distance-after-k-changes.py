class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        

        goals = {"NE", "NW", "SE", "SW"}
        convert = {"N": "S", "S": "N", "E": "W", "W": "E"}
        xdir = {"N": 0, "S": 0, "E": 1, "W": -1}
        ydir = {"N": 1, "S": -1, "E":0, "W": 0} 
        ans = 0
        for goal in goals:
            currx = curry = 0
            remain = k
            for direction in s:
                if direction not in goal and remain:
                    direction = convert[direction]
                    remain -= 1
                currx += xdir[direction]
                curry += ydir[direction]
                ans = max(ans, abs(currx) + abs(curry))

        return ans

        
