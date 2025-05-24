class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        
        queries.sort()
        candidates = []
        chosen = []
        num_chosen = 0

        index = 0
        q_index = 0 
        n = len(nums)
        m = len(queries)
        while index < n:
            while q_index < m and queries[q_index][0] <= index: 
                heappush(candidates, -queries[q_index][1])
                q_index += 1

            num = nums[index]

            while candidates and len(chosen) < num:
                val = heappop(candidates)
                val = -val
                if val >= index:
                    heappush(chosen, val)
                    num_chosen += 1

            if len(chosen) < num:
                return -1

            nums[index] = 0

            while chosen and chosen[0] <= index:
                heappop(chosen)

            index += 1

        return len(queries) - num_chosen

        
        