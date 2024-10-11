class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        
        options = []
        for num in nums:
            curr = []
            while num > 0:
                curr.append(str(num & 1))
                num = num >> 1
            curr.reverse()
            options.append("".join(curr))

        def compare(a,b):
            if a+b > b+a:
                return 1
            else:
                return -1

        options.sort(key=cmp_to_key(compare))
        ans = ""
        while options:
            curr = options.pop()
            ans += curr

        ans = int(ans, 2)
        return ans
