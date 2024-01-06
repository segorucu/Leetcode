class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        stack = sorted(zip(startTime, endTime, profit))

        n = len(stack)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0

            skip = dp(i+1)
            left = i+1
            right = n-1
            while left <= right:
                mid = (left+right) // 2
                if stack[mid][0] >= stack[i][1]:
                    right = mid - 1
                else:
                    left = mid + 1
            # while j < n and stack[i][1] > stack[j][0]:
            #     j+=1
            take = dp(left) + stack[i][2]

            return max(skip,take)

        return dp(0)