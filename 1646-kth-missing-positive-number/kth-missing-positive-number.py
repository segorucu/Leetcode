class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        

        curr = 1
        for num in arr:
            while curr < num:
                k -= 1
                if k == 0:
                    return curr
                curr += 1
            curr = num+1

        while k > 1:
            curr += 1
            k -= 1
        return curr
