class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        if k == 0:
            return sum(sweetness)

        def check(target):
            tot = 0
            sm = 0
            for sweet in sweetness:
                sm += sweet
                if sm >= target:
                    tot += 1
                    sm = 0
            return tot >= k + 1

        left = 1
        right = sum(sweetness)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right