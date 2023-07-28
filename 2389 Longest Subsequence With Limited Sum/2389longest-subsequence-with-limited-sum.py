class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)

        nums.sort()
        presum = [0]
        for num in nums:
            presum.append(presum[-1]+num)
        # presum.pop(0)
        # print(n)

        def binarysearch(presum,target):
            left = 1
            right = n
            while left <= right:
                mid = (left + right) // 2
                if target >= presum[mid]:
                    left = mid + 1
                elif target < presum[mid]:
                    right = mid - 1
            return left-1

        ans = []
        for query in queries:
            ans.append(binarysearch(presum,query))

        return ans