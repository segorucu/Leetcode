class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []

        val = 2
        ans = []
        while finalSum > 0:
            ans.append(val)
            finalSum -= val
            if finalSum <= ans[-1]:
                ans[-1] += finalSum
                finalSum = 0
            val += 2
            

        return ans
