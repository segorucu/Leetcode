class Solution:
    def racecar(self, target: int) -> int:
        
        queue = []
        queue.append((0,1,0))

        curr = []
        while queue:
            pos, speed, steps = queue.pop()
            if pos == target:
                return steps

            curr.append((pos + speed, speed * 2, steps + 1))
            if pos+speed > target and speed > 0:
                curr.append((pos, -1, steps +1))
            elif pos+speed < target and speed < 0:
                curr.append((pos, 1, steps +1))

            if not queue:
                queue = curr
                curr = []

