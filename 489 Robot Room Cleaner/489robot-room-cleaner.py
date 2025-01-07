# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        moves = [(-1,0),(0,1),(1,0),(0,-1)]

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(x, y, direction):
            visited.add((x,y))
            robot.clean()

            for i in range(4):
                new_direction = (direction + i) % 4
                new_x = x + moves[new_direction][0]
                new_y = y + moves[new_direction][1]

                if (new_x, new_y) not in visited and robot.move():
                    dfs(new_x, new_y, new_direction)
                    go_back()

                robot.turnRight()
 
        visited = set()
        dfs(0, 0, 0)
        