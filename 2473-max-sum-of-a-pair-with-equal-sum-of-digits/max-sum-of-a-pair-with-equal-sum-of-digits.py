class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        

        graph = collections.defaultdict(list)
        for num in nums:
            total = 0
            curr = num
            while curr:
                total += curr % 10
                curr = curr // 10
            graph[total].append(num)

        ans = -1
        for k,v in graph.items():
            if len(v) >= 2:
                v.sort()
                ans = max(ans,v[-2]+v[-1])

        return ans