class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left = 0
        n = len(citations)
        right = len(citations) - 1
        

        while left <= right:
            mid = (left + right) // 2
            h = n - mid
            if h == citations[mid]:
                return h
            elif h > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return n - left

        # left = 0
        # right = 0
        # mid = 0
        # h = 1
