from collections import defaultdict
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:

        tab = defaultdict(list)
        for li, hi in rectangles:
            tab[hi].append(li)

        for key in tab.keys():
            tab[key].sort(reverse=True)

        ans = [0] * len(points)

        i = 0
        for i, point in enumerate(points):
            xj, yj = point
            for height in tab.keys():
                if height < yj:
                    continue
                arr = tab[height]
                left = 0
                right = len(arr) - 1
                res = 0
                while left <= right:
                    mid = (left + right) // 2
                    if arr[mid] >= xj:
                        left = mid + 1
                    else:
                        right = mid - 1
                ans[i] += left

        return ans

            