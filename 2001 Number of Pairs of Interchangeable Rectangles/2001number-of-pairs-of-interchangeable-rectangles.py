class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        ratio = collections.defaultdict(int)
        ans = 0
        for a,b in rectangles:
            rat = a / b
            ans += ratio[rat]
            ratio[rat] += 1

        return ans
        