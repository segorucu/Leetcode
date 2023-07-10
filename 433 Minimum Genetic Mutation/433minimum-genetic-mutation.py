from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        options = ['A','C','G','T']
        queue = deque()
        seen = set()
        seen.add(startGene)
        queue.append((startGene,0))

        while queue:
            state, steps = queue.popleft()
            if state == endGene:
                return steps
            for i in range(8):
                for move in options:
                    candidate = state[0:i] + move + state[i+1:]
                    if candidate not in seen and candidate in bank:
                        seen.add(candidate)
                        queue.append((candidate,steps+1))

        return -1
