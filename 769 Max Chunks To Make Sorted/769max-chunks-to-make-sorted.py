class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        one = list(accumulate(arr))
        arr.sort()
        two = list(accumulate(arr))
        # print(one,two)
        tot = 0
        for a,b in zip(one,two):
            # print(a,b)
            if a == b:
                tot += 1
        return tot

        