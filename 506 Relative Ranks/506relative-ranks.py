class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        arr = []
        for i, val in enumerate(score):
            arr.append((val,i))

        arr.sort(reverse = True)

        n = len(score)
        ans = n * [None]
        init = ["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(n):
            if i < 3:
                ans[arr[i][1]] = init[i]
            else:
                ans[arr[i][1]] = str(i+1)


        return ans
        