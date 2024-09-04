class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        right = {"N":"E", "E":"S", "S":"W", "W":"N"}
        left =  {"E":"N", "S":"E", "W":"S", "N":"W"}
        banned = set()
        for x,y in obstacles:
            banned.add((x,y))

        ans = 0
        direction = "N"
        x = y = 0
        for c in commands:
            if c == -1:
                direction = right[direction]
            elif c == -2:
                direction = left[direction]
            else:
                while c > 0:
                    nx, ny = x, y
                    if direction == "N":
                        ny += 1
                    elif direction == "S":
                        ny -= 1
                    elif direction == "E":
                        nx += 1
                    else:
                        nx -= 1
                    c -= 1
                    if (nx,ny) in banned:
                        break
                    x, y = nx, ny
                ans = max(ans,x**2+y**2)
        return ans

