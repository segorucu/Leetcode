class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        curr = (0,0)
        for command in commands:
            if command == "UP":
                curr = (curr[0]-1,curr[1])
            elif command == "DOWN":
                curr = (curr[0]+1,curr[1])
            elif command == "RIGHT":
                curr = (curr[0],curr[1]+1)
            elif command == "LEFT":
                curr = (curr[0],curr[1]-1)

        return curr[0]*n+curr[1]