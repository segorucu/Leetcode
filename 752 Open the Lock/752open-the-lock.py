from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        
        seen = set(deadends)
        queue = deque()
        queue.append(("0000",0))
        seen.add("0000")

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            for i in range(4):
                num = int(state[i])
                for j in [-1,1]:
                    num1 = (num + j) % 10
                    new = state[0:i] + str(num1) + state[i+1:]
                    if new not in seen:
                        seen.add(new)
                        queue.append((new,steps+1))
                    
        

        return -1