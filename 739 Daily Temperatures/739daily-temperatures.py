from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        answer = n *[0]

        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                i0, t0 = stack.pop()
                answer[i0] = i - i0
            stack.append((i,t))


        return answer
        