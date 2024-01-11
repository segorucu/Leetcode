class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        ans = 0
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right) // 2
            count = n-mid
            if citations[mid] >= count:
                ans = max(ans,count)
                right = mid - 1
            else:
                left = mid + 1

        return ans
        