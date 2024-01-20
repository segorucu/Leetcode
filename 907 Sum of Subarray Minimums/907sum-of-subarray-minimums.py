from functools import cache
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        modulo = 10**9 + 7
        n = len(arr)
        ans = 0

        left = n * [-1]
        right = n * [n]

        stack = []
        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] >= val:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        for i, val in enumerate(arr):
            ans += (i-left[i]) * (right[i]-i) * val % modulo

        return ans % modulo
        