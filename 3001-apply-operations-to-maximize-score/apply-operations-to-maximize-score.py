class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        scores = []
        for n in nums:
            score = 0
            for i in range(2,int(sqrt(n)+1)):
                if n % i == 0:
                    score += 1
                    while n % i == 0:
                        n = n // i
            if n > 1:
                score += 1
            scores.append(score)

        left = N * [-1]
        right = N * [N]
        stack = []
        for i,score in enumerate(scores):
            while stack and scores[stack[-1]] < score:
                index = stack.pop()
                right[index] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        min_heap = []
        for i,num in enumerate(nums):
            heappush(min_heap,(-num,i))

        MOD = 10**9+7
        res = 1
        while k > 0:
            num, i = heappop(min_heap)
            num = -num
            l = i - left[i]
            r = right[i] - i
            count = l * r
            count = min(k, count)
            res = (res * pow(num, count, MOD)) % MOD
            k -= count
            
        return res