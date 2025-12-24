class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        capacity.sort()
        sm = sum(apple)
        ans = 0
        while sm > 0:
            sm -= capacity.pop()
            ans += 1

        return ans
