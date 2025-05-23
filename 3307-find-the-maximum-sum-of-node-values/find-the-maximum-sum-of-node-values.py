class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        tot = 0
        count = 0
        mindiff = float("inf")
        for num in nums:
            cand = num ^ k
            # print(num,cand)
            if cand > num:
                tot += cand
                count += 1
            else:
                tot += num
            # print(abs(cand-num))
            if abs(cand-num) < mindiff:
                    mindiff = abs(cand - num)
        #     print(mindiff)

        # print(tot)
        if count % 2:
            tot -= mindiff
        return tot
        