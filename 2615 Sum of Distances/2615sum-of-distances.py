class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        prefix = collections.defaultdict(list)
        indexmp = collections.defaultdict(list)

        for i, num in enumerate(nums):
            if num in prefix:
                prefix[num].append(prefix[num][-1]+i)
            else:
                prefix[num].append(i)
            indexmp[num].append(i)

        n = len(nums)
        ans = n * [0]

        for num, values in prefix.items():
            n = len(values)

            for i in range(n):
                ind = indexmp[num][i]
                ans[ind] = (prefix[num][-1] - prefix[num][i]) - (n - i - 1) * ind
                if i > 0:
                    ans[ind] += (i * ind - prefix[num][i-1])

        return ans
        