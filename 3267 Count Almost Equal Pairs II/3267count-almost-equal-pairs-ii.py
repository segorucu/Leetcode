class Solution:
    def countPairs(self, nums: List[int]) -> int:
        

        n = len(nums)
        def permute(num):
            options = set()
            options.add(num)
            num = str(num)
            num = num.zfill(7)
            m = len(num)
            for i in range(m):
                for j in range(i+1,m):
                    tmp = num[0:i] + num[j] + num[i+1:j] + num[i] + num[j+1:]
                    tmp = int(tmp)
                    options.add(tmp)
            return options

        counter = collections.defaultdict(int)
        ans = 0
        for i, num in enumerate(nums):
            options = permute(num)
            options2 = set()
            for val in options:
                options2.update(permute(val))
            for val in options2:
                ans += counter[val]
            counter[num] += 1

        return ans