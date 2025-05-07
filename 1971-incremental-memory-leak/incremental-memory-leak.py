class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        
        time = 1
        while time <= max(memory1, memory2):
            if memory1 >= memory2:
                memory1 -= time
            else:
                memory2 -= time
            time += 1
        
        return time, memory1, memory2