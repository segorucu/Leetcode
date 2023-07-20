class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        cancelled = 0
        for c in asteroids:
            while stack and stack[-1] > 0 and c < 0:
                if stack[-1] + c == 0:
                    stack.pop()
                    cancelled = 1
                    break
                elif stack[-1] + c > 0:
                    cancelled = 1
                    break
                elif stack[-1] + c < 0:
                    stack.pop()
            if cancelled == 0:
                stack.append(c)
            cancelled = 0
        return stack
                